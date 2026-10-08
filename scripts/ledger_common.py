#!/usr/bin/env python3
"""Judgment ledger helpers. Stdlib only.

The ledger is a measurement layer. It does not add fields to routing.jsonl
and it is not a tenth brain file. See docs/judgment_ledger.md.
"""
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ROOT_ROUTING = "brain/routing.jsonl"
ROOT_THESES = "brain/theses.json"
ROOT_INTAKE = ("intake/collected.jsonl", "intake/user.jsonl")
LEDGER_PATH = "ledger/judgment_ledger.jsonl"
SUMMARY_PATH = "ledger/score_summary.json"
SCORECARD_PATH = "ledger/scorecard.json"

STANCES = ("긍정", "중립", "부정", "헤지")
MARKETS = ("KR", "US", "JP", "OTHER")
SCORE_MODES = ("excess", "manual")
HORIZONS = (("30d", 30), ("90d", 90))
# Trailing ⓐ with no ⓑ. Threshold is a proposal — see the design doc.
CONFIRM_STREAK_WARN = 5
# Directional hit uses a strict sign. Zero excess is a miss. 중립 is no-call.
ZERO_BAND = 0.0

# October 2026 is still US EDT. zoneinfo handles the November switch.
SESSION_CLOSE = {
    "KR": (ZoneInfo("Asia/Seoul"), 15, 30),
    # Naver stockExchangeType.endTime for TYO is 1530. Cash Nikkei can print earlier;
    # 15:30 avoids treating a midday bar as the close.
    "JP": (ZoneInfo("Asia/Tokyo"), 15, 30),
    "US": (ZoneInfo("America/New_York"), 16, 0),
}

NAVER_UA = {"User-Agent": "Mozilla/5.0", "Referer": "https://m.stock.naver.com/"}
FRED_UA = {"User-Agent": "research-archive contact kenchoi@keywestaim.com"}

# Distribution and shorteners are not original sources.
# Distribution hosts and shorteners. vo.la showed up as a Meritz note wrapper on 2026-10-08.
SKIP_HOST_SUFFIXES = (
    "t.me", "telegram.me", "telegram.org", "cutt.ly", "bit.ly", "tinyurl.com", "t.co", "vo.la",
)
# Large KRW figures that identify a print. 50조 drops market-cap crumbs in 억 and message ids.
ANCHOR_MIN_JO = 50.0
ANCHOR_TOL_JO = 0.6
NAME_RE = re.compile(r"삼성전자|SK하이닉스|하이닉스|브로드컴|오라클|스페이스X|대덕전자|심텍|해성디에스|005930|000660|353200|222800|195870")
URL_RE = re.compile(r"https?://[^\s<>\]\)\"']+")
RCP_RE = re.compile(r"rcpNo[=:](\d{10,})", re.I)
HANGUL_RE = re.compile(r"[가-힣]")
MATERIAL_RE = re.compile(
    r"(?P<num>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)\s*(?P<unit>조|억|%|bp|Gbps|GB|MW)?"
)
MATERIAL_UNITS = {"조", "억", "%", "bp", "Gbps", "GB", "MW"}

FORBIDDEN_KEYS = {
    "disposition", "theses_change", "portfolio_change", "weight", "weights",
    "shares", "quantity", "stop", "stops", "holding", "holdings", "order",
    "orders", "sizing", "size",
}

ID_RE = re.compile(r"^j-\d{8}-\d{2,3}$")
ROUTING_ID_RE = re.compile(r"^r-\d{8}-\d{2,3}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
OPS = {"lt", "lte", "gt", "gte", "eq", "neq"}


def read_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def load_routing_index(path=ROOT_ROUTING):
    return {r["id"]: r for r in read_jsonl(path)}


def load_intake_index(paths=ROOT_INTAKE):
    out = {}
    for path in paths:
        try:
            for row in read_jsonl(path):
                if row.get("id"):
                    out[row["id"]] = row
        except OSError:
            continue
    return out


def load_thesis_index(path=ROOT_THESES):
    pages = json.load(open(path, encoding="utf-8"))["pages"]
    return {p: {t["id"]: t for t in pg.get("theses") or []} for p, pg in pages.items()}


def http_json(url, headers, timeout=20):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def naver_daily(kind, code, start_yyyymmdd, end_yyyymmdd):
    """kind is domestic/item, domestic/index, foreign/item, or foreign/index.

    Same hosts update_prices.py and intake/collect_sources.py already use.
    No API key.
    """
    url = (
        f"https://api.stock.naver.com/chart/{kind}/{code}/day"
        f"?startDateTime={start_yyyymmdd}&endDateTime={end_yyyymmdd}"
    )
    rows = http_json(url, NAVER_UA)
    if not isinstance(rows, list):
        return []
    out = []
    for row in rows:
        try:
            out.append((str(row["localDate"]), float(row["closePrice"])))
        except (KeyError, TypeError, ValueError):
            continue
    out.sort()
    return out


def fred_series(series_id):
    """FRED graph CSV. No API key. Same endpoint as intake/collect_sources.fred_csv."""
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={urllib.parse.quote(series_id)}"
    req = urllib.request.Request(url, headers=FRED_UA)
    with urllib.request.urlopen(req, timeout=20) as resp:
        text = resp.read().decode()
    out = []
    for line in text.strip().splitlines()[1:]:
        date, value = line.split(",", 1)
        out.append((date, None if value in ("", ".") else float(value)))
    return out


def session_complete(market, bar_yyyymmdd, now):
    """True when the regular session for that calendar bar has finished.

    A same-day Naver bar while the session is open is the last print, not the close.
    Early closes are not modeled.
    """
    if market not in SESSION_CLOSE:
        return True
    tz, hour, minute = SESSION_CLOSE[market]
    y, m, d = int(bar_yyyymmdd[:4]), int(bar_yyyymmdd[4:6]), int(bar_yyyymmdd[6:8])
    close_at = datetime(y, m, d, hour, minute, tzinfo=tz)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    return now >= close_at


def last_completed_close(series, asof_yyyymmdd, market, now):
    """Last (date, close) on or before asof whose session is complete. None if none."""
    chosen = None
    for date, close in series:
        if date > asof_yyyymmdd:
            continue
        if session_complete(market, date, now):
            chosen = (date, close)
    return chosen


def iso_date(yyyymmdd):
    return f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:8]}"


def yyyymmdd(iso):
    return iso.replace("-", "")


def add_days(iso, days):
    base = datetime.strptime(iso, "%Y-%m-%d").date()
    return (base + timedelta(days=days)).isoformat()


def endpoint_for(kind, code):
    return f"https://api.stock.naver.com/chart/{kind}/{code}/day"


# --- source dedupe ---------------------------------------------------------

def _host(url):
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    return host


def _skip_host(host):
    return any(host == s or host.endswith("." + s) for s in SKIP_HOST_SUFFIXES)


def normalize_url(url):
    parts = urllib.parse.urlsplit(url)
    host = _host(url)
    path = parts.path.rstrip("/")
    query = urllib.parse.parse_qs(parts.query)
    # Filing path is shared by every DART viewer. The receipt number is the document.
    if query.get("rcpNo"):
        return f"{host}{path}?rcpNo={query['rcpNo'][0]}"
    return host + path


def external_urls(text):
    found = []
    for raw in URL_RE.findall(text or ""):
        raw = raw.rstrip(".,);]")
        host = _host(raw)
        if not host or _skip_host(host):
            continue
        found.append(normalize_url(raw))
    return found


def _strip_skipped_urls(text):
    def repl(match):
        raw = match.group(0).rstrip(".,);]")
        return " " if _skip_host(_host(raw)) else match.group(0)
    return URL_RE.sub(repl, text or "")


def material_signature(text):
    """Sorted (number, unit) pairs that look like claim figures, not years or ids."""
    sig = []
    for match in MATERIAL_RE.finditer(_strip_skipped_urls(text)):
        raw = match.group("num").replace(",", "")
        unit = match.group("unit") or ""
        try:
            num = round(float(raw), 2)
        except ValueError:
            continue
        if unit not in MATERIAL_UNITS:
            # Bare years and small counts are not a story fingerprint.
            if num < 100 or (1900 <= num <= 2100 and num == int(num)):
                continue
            unit = ""
        sig.append((num, unit))
    return tuple(sorted(set(sig)))


def story_anchors(text):
    """Headline KRW amounts in 조, rounded to 0.1. 억 figures are converted (1조 = 10,000억)."""
    cleaned = _strip_skipped_urls(text)
    anchors = set()
    for match in re.finditer(r"(\d+(?:\.\d+)?)\s*조", cleaned):
        value = float(match.group(1))
        if value >= ANCHOR_MIN_JO:
            anchors.add(round(value, 1))
    for match in re.finditer(r"(\d{1,3}(?:,\d{3})+|\d+)\s*억", cleaned):
        value = float(match.group(1).replace(",", "")) / 10000.0
        if value >= ANCHOR_MIN_JO:
            anchors.add(round(value, 1))
    return anchors


def _anchor_hits(left, right, tol=ANCHOR_TOL_JO):
    used = set()
    hits = 0
    for value in left:
        for i, other in enumerate(right):
            if i in used:
                continue
            if abs(value - other) <= tol:
                used.add(i)
                hits += 1
                break
    return hits


def _blob(rec):
    return "\n".join(str(rec.get(k) or "") for k in ("subject", "text", "url"))


def origin_of_record(rec):
    """One intake row -> origin key. URL beats a numeric fingerprint beats the channel."""
    blob = _blob(rec)
    urls = external_urls(blob)
    rcps = RCP_RE.findall(blob)
    sig = material_signature(blob)
    if urls:
        key, kind = "url:" + urls[0], "url"
    elif rcps:
        key, kind = "dart:" + rcps[0], "filing"
    elif len(sig) >= 2:
        key = "num:" + "|".join(f"{n:g}{u}" for n, u in sig)
        kind = "numeric"
    else:
        channel = rec.get("channel") or rec.get("host") or "unknown"
        mid = rec.get("message_id") or rec.get("id")
        key, kind = f"channel:{channel}:{mid}", "channel"
    return {"key": key, "kind": kind, "signature": sig, "id": rec.get("id"), "channel": rec.get("channel")}


def cluster_records(records):
    """Collapse reposts inside one claim's intake rows.

    Merge rules (v1):
    - identical external URL or identical DART rcpNo -> one origin
    - url-less rows with an equal material signature -> one origin
    - rows that share two headline KRW anchors (>=50조, 0.6조 tolerance),
      or a single anchor that close-matches a richer print of the same name,
      are the same story. A DART url in the group wins the key.
    - an analyst note that only shares one anchor and has its own extra
      anchors does not merge (107.4조 cited inside a different argument)
    Cross-claim linking is exact URL / rcp only. See design doc.
    """
    parsed = [origin_of_record(r) for r in records]
    blobs = [_blob(r) for r in records]
    anchors = [story_anchors(b) for b in blobs]
    names = [set(NAME_RE.findall(b)) for b in blobs]
    parent = {i: i for i in range(len(parsed))}

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    by_key = {}
    by_sig = {}
    for i, item in enumerate(parsed):
        by_key.setdefault(item["key"], []).append(i)
        if item["kind"] == "numeric" and item["signature"]:
            by_sig.setdefault(item["signature"], []).append(i)
    for idxs in by_key.values():
        for j in idxs[1:]:
            union(idxs[0], j)
    for sig, idxs in by_sig.items():
        for j in idxs[1:]:
            union(idxs[0], j)
        # Equal signature only: pull a numeric row onto a URL row with the same signature.
        for i, item in enumerate(parsed):
            if item["kind"] in {"url", "filing"} and item["signature"] == sig and idxs:
                union(i, idxs[0])
    for i in range(len(parsed)):
        for j in range(i + 1, len(parsed)):
            if not anchors[i] or not anchors[j]:
                continue
            hits = _anchor_hits(anchors[i], anchors[j])
            if hits >= 2:
                union(i, j)
                continue
            smaller, larger = (anchors[i], anchors[j]) if len(anchors[i]) <= len(anchors[j]) else (anchors[j], anchors[i])
            if len(smaller) == 1 and hits == 1 and names[i] & names[j] and len(larger) >= 2:
                union(i, j)

    groups = {}
    for i, item in enumerate(parsed):
        groups.setdefault(find(i), []).append(item)
    origins = []
    for members in groups.values():
        # Prefer a url/filing key as the group's name.
        def _rank(member):
            if "dart.fss.or.kr" in member["key"]:
                return (0, member["key"])
            return ({"filing": 1, "url": 2, "numeric": 3, "channel": 4}[member["kind"]], member["key"])
        head = sorted(members, key=_rank)[0]
        if "dart.fss.or.kr" in head["key"]:
            head = dict(head)
            head["kind"] = "filing"
        channels = sorted({m["channel"] for m in members if m.get("channel")})
        origins.append({
            "key": head["key"],
            "kind": head["kind"],
            "n_items": len(members),
            "intake": [m["id"] for m in members if m.get("id")],
            "channels": channels,
        })
    origins.sort(key=lambda o: o["key"])
    return {
        "intake_n": len(records),
        "independent_n": len(origins),
        "origins": origins,
    }


def cross_claim_duplicates(rows):
    """Exact URL/filing keys shared by more than one ledger row. Numeric keys stay local."""
    seen = {}
    for row in rows:
        for origin in (row.get("evidence") or {}).get("origins") or []:
            if origin.get("kind") not in {"url", "filing"}:
                continue
            seen.setdefault(origin["key"], []).append(row["id"])
    return {k: v for k, v in seen.items() if len(set(v)) > 1}


# --- scoring ---------------------------------------------------------------

def compare(value, op, threshold):
    if op == "lt":
        return value < threshold
    if op == "lte":
        return value <= threshold
    if op == "gt":
        return value > threshold
    if op == "gte":
        return value >= threshold
    if op == "eq":
        return value == threshold
    if op == "neq":
        return value != threshold
    raise ValueError(op)


def directional_verdict(stance, excess, band=ZERO_BAND):
    """Sign of excess return versus the benchmark. Not a position size."""
    if stance == "중립":
        return "no-call"
    if stance == "헤지":
        return "manual"
    if excess is None:
        return "pending"
    if stance == "긍정":
        return "hit" if excess > band else "miss"
    if stance == "부정":
        return "hit" if excess < -band else "miss"
    return "pending"


def close_on_or_before(series, iso):
    target = yyyymmdd(iso)
    chosen = None
    for date, close in series:
        if date <= target:
            chosen = (date, close)
        else:
            break
    return chosen


def score_horizon(stance, score_mode, ref_price, stock_series, bench_series, ref_asof, horizon_days, today):
    due = add_days(ref_asof, horizon_days)
    base = {
        "due": due,
        "status": "pending",
        "ret": None,
        "bench_ret": None,
        "excess": None,
        "px_asof": None,
        "bench_asof": None,
        "verdict": "pending",
    }
    if today < due:
        return base
    if score_mode == "manual":
        base["status"] = "manual"
        base["verdict"] = "manual"
        return base
    if ref_price in (None, 0):
        base["status"] = "unverified"
        base["verdict"] = "unverified"
        return base
    stock = close_on_or_before(stock_series or [], due)
    bench = close_on_or_before(bench_series or [], due)
    if not stock or not bench:
        base["status"] = "unverified"
        base["verdict"] = "unverified"
        return base
    # Benchmark reference is the benchmark close on the same ref date.
    bench_ref = close_on_or_before(bench_series, ref_asof)
    if not bench_ref or bench_ref[1] == 0:
        base["status"] = "unverified"
        base["verdict"] = "unverified"
        return base
    ret = stock[1] / ref_price - 1
    bench_ret = bench[1] / bench_ref[1] - 1
    excess = ret - bench_ret
    base.update({
        "status": "scored",
        "ret": round(ret, 6),
        "bench_ret": round(bench_ret, 6),
        "excess": round(excess, 6),
        "px_asof": iso_date(stock[0]),
        "bench_asof": iso_date(bench[0]),
        "verdict": directional_verdict(stance, excess),
    })
    return base


def eval_price_break(cond, series, today):
    """Price/macro conditions the scorer can see. Everything else stays manual."""
    check = cond.get("check") or "manual"
    if check == "manual":
        return {"status": "manual", "observed": None}
    if check not in {"price", "macro"}:
        return {"status": "manual", "observed": None}
    deadline = cond.get("deadline")
    observed = None
    if series:
        # last point on or before today
        chosen = close_on_or_before(series, today)
        if chosen:
            observed = chosen[1]
    if observed is None:
        return {"status": "unverified", "observed": None}
    fired = compare(observed, cond["op"], cond["threshold"])
    if fired:
        return {"status": "fired", "observed": observed}
    if deadline and today > deadline:
        return {"status": "ok", "observed": observed}
    return {"status": "pending", "observed": observed}


def confirm_stats(thesis):
    """ⓐ confirms versus ⓑ refutes, plus the trailing confirm-only streak."""
    confirm = refute = 0
    streak = 0
    counting = True
    for entry in reversed(thesis.get("log") or []):
        mark = str(entry.get("mark") or "")
        is_refute = "ⓑ" in mark
        is_confirm = "ⓐ" in mark and not is_refute
        if is_confirm:
            confirm += 1
            if counting:
                streak += 1
        elif is_refute:
            refute += 1
            counting = False
        else:
            counting = False
    # The loop above only counts the tail. Recount full history for the totals.
    confirm = refute = 0
    for entry in thesis.get("log") or []:
        mark = str(entry.get("mark") or "")
        if "ⓑ" in mark:
            refute += 1
        elif "ⓐ" in mark:
            confirm += 1
    return {
        "confirm": confirm,
        "refute": refute,
        "confirm_streak": streak,
        "priced_in_warning": streak >= CONFIRM_STREAK_WARN,
    }


def build_scorecard(ledger_rows, thesis_index):
    """Per page#T: confirm/refute from theses.log, breaks_if from the ledger.

    Warning flags are included even when the thesis has no ledger row yet.
    The HTML card renderer is intentionally not changed in this scaffold.
    """
    linked = {}
    for row in ledger_rows:
        for page in row.get("pages") or []:
            linked.setdefault(page, []).append(row)
    cards = []
    seen = set()

    def add(page, thesis_id, thesis):
        key = f"{page}#{thesis_id}"
        if key in seen or thesis is None:
            return
        seen.add(key)
        stats = confirm_stats(thesis)
        rows = []
        # Ledger rows may point at page#T.
        for row in linked.get(key, []):
            rows.append(row)
        breaks = []
        for row in rows:
            for cond in row.get("breaks_if") or []:
                status = None
                if row.get("scores"):
                    for item in row["scores"].get("breaks_if") or []:
                        if item.get("text") == cond.get("text"):
                            status = item.get("status")
                breaks.append({
                    "ledger_id": row["id"],
                    "routing_id": row.get("routing_id"),
                    "ticker": row.get("ticker"),
                    "text": cond.get("text"),
                    "check": cond.get("check"),
                    "status": status or cond.get("check") or "manual",
                    "deadline": cond.get("deadline"),
                })
        if not stats["priced_in_warning"] and not rows:
            return
        cards.append({
            "page": page,
            "thesis": thesis_id,
            "status": thesis.get("status"),
            "confirm": stats["confirm"],
            "refute": stats["refute"],
            "confirm_streak": stats["confirm_streak"],
            "priced_in_warning": stats["priced_in_warning"],
            "ledger_n": len(rows),
            "breaks_if": breaks,
        })

    for page, theses in thesis_index.items():
        for thesis_id, thesis in theses.items():
            add(page, thesis_id, thesis)
    for key in linked:
        if "#" not in key or key in seen:
            continue
        page, thesis_id = key.split("#", 1)
        thesis = thesis_index.get(page, {}).get(thesis_id)
        add(page, thesis_id, thesis)
    cards.sort(key=lambda c: (-int(c["priced_in_warning"]), -c["confirm_streak"], c["page"], c["thesis"]))
    return cards


def summarize(ledger_rows, scorecard):
    def blank():
        return {"n": 0, "hit": 0, "miss": 0, "pending": 0, "no_call": 0, "manual": 0, "unverified": 0, "hit_rate": None}

    def add(bucket, verdict):
        bucket["n"] += 1
        if verdict == "hit":
            bucket["hit"] += 1
        elif verdict == "miss":
            bucket["miss"] += 1
        elif verdict == "no-call":
            bucket["no_call"] += 1
        elif verdict == "manual":
            bucket["manual"] += 1
        elif verdict == "unverified":
            bucket["unverified"] += 1
        else:
            bucket["pending"] += 1

    def finish(bucket):
        den = bucket["hit"] + bucket["miss"]
        bucket["hit_rate"] = round(bucket["hit"] / den, 4) if den else None
        return bucket

    by_stance = {s: blank() for s in STANCES}
    by_lead = {}
    by_page = {}
    intake_n = independent_n = 0
    for row in ledger_rows:
        ev = row.get("evidence") or {}
        intake_n += ev.get("intake_n") or 0
        independent_n += ev.get("independent_n") or 0
        scores = (row.get("scores") or {}).get("horizons") or {}
        # Calibration uses the longer horizon once it exists, else 30d, else pending.
        verdict = "pending"
        if scores.get("90d", {}).get("status") == "scored":
            verdict = scores["90d"]["verdict"]
        elif scores.get("30d", {}).get("status") == "scored":
            verdict = scores["30d"]["verdict"]
        elif row.get("score_mode") == "manual":
            verdict = "manual"
        elif scores:
            verdict = scores.get("30d", {}).get("verdict") or "pending"
        add(by_stance[row["stance"]], verdict)
        lead = row.get("lead") or "unknown"
        add(by_lead.setdefault(lead, blank()), verdict)
        for page in row.get("pages") or []:
            add(by_page.setdefault(page, blank()), verdict)
    warnings = [c for c in scorecard if c.get("priced_in_warning")]
    return {
        "ledger_n": len(ledger_rows),
        "by_stance": {k: finish(v) for k, v in by_stance.items()},
        "by_lead": {k: finish(v) for k, v in sorted(by_lead.items())},
        "by_page": {k: finish(v) for k, v in sorted(by_page.items())},
        "evidence": {
            "intake_rows_summed": intake_n,
            "independent_origins_summed": independent_n,
            "note": "행마다 센 합이다. 행 사이 URL 공유는 cross_claim_duplicates.",
        },
        "cross_claim_duplicate_urls": cross_claim_duplicates(ledger_rows),
        "priced_in_warning_n": len(warnings),
        "priced_in_warnings": [
            {"page": c["page"], "thesis": c["thesis"], "confirm_streak": c["confirm_streak"],
             "confirm": c["confirm"], "refute": c["refute"]}
            for c in warnings
        ],
    }


# --- validation ------------------------------------------------------------

def forbidden_keys(obj, prefix=""):
    found = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            path = f"{prefix}.{key}" if prefix else key
            if key in FORBIDDEN_KEYS:
                found.append(path)
            found.extend(forbidden_keys(value, path))
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            found.extend(forbidden_keys(value, f"{prefix}[{i}]"))
    return found


def validate_row(row, routing_ids, thesis_index):
    errors = []
    rid = row.get("id", "?")
    if not ID_RE.match(str(row.get("id", ""))):
        errors.append(f"{rid}: id 형식 j-YYYYMMDD-NN 아님")
    routing_id = row.get("routing_id")
    if not ROUTING_ID_RE.match(str(routing_id or "")):
        errors.append(f"{rid}: routing_id 형식")
    elif routing_id not in routing_ids:
        errors.append(f"{rid}: routing_id {routing_id} 가 routing.jsonl 에 없다")
    if not DATE_RE.match(str(row.get("date", ""))):
        errors.append(f"{rid}: date 형식")
    if row.get("stance") not in STANCES:
        errors.append(f"{rid}: stance {row.get('stance')!r}")
    if row.get("market") not in MARKETS:
        errors.append(f"{rid}: market")
    if row.get("score_mode") not in SCORE_MODES:
        errors.append(f"{rid}: score_mode")
    if not str(row.get("ticker") or "").strip():
        errors.append(f"{rid}: ticker 비었다")
    if not HANGUL_RE.search(str(row.get("claim_ko") or "")):
        errors.append(f"{rid}: claim_ko 에 한국어가 없다")
    ref = row.get("ref") or {}
    price = ref.get("price", "missing")
    if price is None and not ref.get("unverified_reason"):
        errors.append(f"{rid}: ref.price 가 null 이면 unverified_reason 이 필요하다")
    elif price not in (None, "missing") and not isinstance(price, (int, float)):
        errors.append(f"{rid}: ref.price 는 수 또는 null")
    if not ref.get("endpoint"):
        errors.append(f"{rid}: ref.endpoint 가 없다 — 시도한 경로를 남긴다")
    horizons = row.get("horizons")
    if horizons != ["30d", "90d"]:
        errors.append(f"{rid}: horizons 는 ['30d','90d']")
    breaks = row.get("breaks_if")
    if not isinstance(breaks, list) or not breaks:
        errors.append(f"{rid}: breaks_if 가 비었다")
    else:
        for cond in breaks:
            if not str(cond.get("text") or "").strip():
                errors.append(f"{rid}: breaks_if.text 비었다")
            if cond.get("check") not in {"manual", "price", "macro"}:
                errors.append(f"{rid}: breaks_if.check")
            if cond.get("check") in {"price", "macro"}:
                if cond.get("op") not in OPS or not isinstance(cond.get("threshold"), (int, float)):
                    errors.append(f"{rid}: price/macro 조건은 op 와 숫자 threshold")
                if cond.get("check") == "macro" and not str(cond.get("metric") or "").startswith("fred:"):
                    errors.append(f"{rid}: macro metric 은 fred:<SERIES>")
    for page in row.get("pages") or []:
        if "#" not in page:
            errors.append(f"{rid}: pages 원소는 page#T")
            continue
        pg, tid = page.split("#", 1)
        if pg not in thesis_index or tid not in thesis_index[pg]:
            errors.append(f"{rid}: pages {page} 실재하지 않음")
    banned = forbidden_keys(row)
    if banned:
        errors.append(f"{rid}: 금지 필드 {banned} — 수량·비중·스톱·집행을 장부에 넣지 않는다")
    return errors
