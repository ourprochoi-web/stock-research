#!/usr/bin/env python3
"""routing.jsonl 의 새 줄이 AGENTS.md §3 계약을 지켰는지 검사한다 — 어기면 exit 1 (커밋·CI 거절).

왜 차단인가(2026-09-25 실측): 훅의 포인터 검사가 「경고만」인 열흘 동안
  · routing 273줄 중 실재 테제에 닿은 것 82(30%) · routed[] 원소 643 중 실재 130(20%)
  · 09-22 이후 Lead 봇 줄 33건 전부 digest-only · routed[] 는 intake 파일 경로 · theses.json 은 사흘간 무변화
경고는 봇이 읽지 않는다. 거절만 읽는다.

2026-09-26 추가 — 테제에 안 걸린 관측은 버리지 않고 entities.companies[KEY].watch[] 에 쌓는다(parked:"entity:<KEY>").
  「판정」만 쌓이고 「종합」이 없던 것이 결정 시점의 그림을 비게 했다. 그래서 접촉 검사는 테제 log[] 또는 엔티티 watch[] 둘 중 하나.

적용 범위: date >= EFFECTIVE 인 줄. 그 전 줄은 레거시로 두고(일괄 마이그레이션 금지) 통계만 찍는다.
용법: check_routing.py [--all] [--effective YYYY-MM-DD]
"""
import collections
import io
import json
import re
import sys
from datetime import date

EFFECTIVE = "2026-09-26"
ROUTING = "brain/routing.jsonl"
THESES = "brain/theses.json"
EVENTS = "brain/events.json"
INTAKE = ("intake/user.jsonl", "intake/collected.jsonl")
BRAIN_JSON = ("brain/theses.json", "brain/facts.json", "brain/entities.json", "brain/events.json",
              "brain/open.json", "brain/regime.json", "brain/mechanisms.json", "brain/portfolio.json")

KINDS = {"route", "observation", "judgment", "verdict", "prediction", "decision", "lesson",
         "correction", "measurement"}
KNOWN_FIELDS = {"id", "date", "kind", "intake", "grade", "claim", "routed", "parked", "verdict", "action",
                "priced_in", "variant", "breaks_if", "resolve_by", "confidence", "source", "corrects",
                "found_by", "outcome", "lesson", "judged_by", "verdict_result", "due", "event", "note",
                "page", "position", "batch", "via", "url", "ref", "tickers", "urls", "cross_ref"}
PARKED = {"open", "regime", "portfolio", "events"}
ENTITY_PREFIX = "entity:"   # parked:"entity:<KEY>" — 테제에 안 걸린 관측을 entities.companies[KEY].watch[] 에 쌓는다(2026-09-26)
WATCH_SOFT_CAP = 12         # watch[] 가 이 수를 넘으면 경고 — 테제로 승격하거나 접을 때다
ENTITIES = "brain/entities.json"
ID_RE = re.compile(r"^r-\d{8}-\d{2,3}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
HANGUL = re.compile(r"[가-힣]")
NEEDS_INTAKE = {"route", "observation", "judgment"}
NEEDS_THREE = {"observation", "judgment"}


def jsonl(path):
    rows, bad = [], []
    try:
        for n, ln in enumerate(io.open(path, encoding="utf-8"), 1):
            if not ln.strip():
                continue
            try:
                rows.append(json.loads(ln))
            except ValueError as e:
                bad.append(f"{path}:{n} JSON 파손 — {e}")
    except OSError:
        pass
    return rows, bad


def main(argv):
    all_rows = "--all" in argv
    eff = EFFECTIVE
    if "--effective" in argv:
        eff = argv[argv.index("--effective") + 1]
    errors, warns = [], []

    # 0. 브레인 JSON 유효성 — 파손은 전부 거절
    for f in BRAIN_JSON:
        try:
            json.load(io.open(f, encoding="utf-8"))
        except (OSError, ValueError) as e:
            errors.append(f"{f} JSON 파손 — {e}")
    if errors:
        return report(errors, warns)

    T = json.load(io.open(THESES, encoding="utf-8"))["pages"]
    tid = {p: {t["id"]: t for t in pg.get("theses", [])} for p, pg in T.items()}
    ENT = json.load(io.open(ENTITIES, encoding="utf-8")).get("companies", {})
    rows, bad = jsonl(ROUTING)
    errors += bad
    intake_ids = set()
    for f in INTAKE:
        r, b = jsonl(f)
        errors += b
        intake_ids |= {x.get("id") for x in r}

    # 1. id 중복 — 날짜 무관(포인터가 어느 줄인지 알 수 없어진다)
    dup = {k: v for k, v in collections.Counter(r.get("id") for r in rows).items() if v > 1}
    for k, v in dup.items():
        errors.append(f"routing id 중복 {k} ×{v}")

    # 2. 새 줄 검사
    new = [r for r in rows if all_rows or str(r.get("date", "")) >= eff]
    touched_ok = touched_total = 0
    for r in new:
        rid = r.get("id", "?")
        tag = f"{rid} «{str(r.get('claim', ''))[:28]}»"
        if not ID_RE.match(str(rid)):
            errors.append(f"{tag}: id 형식 r-YYYYMMDD-NN 아님")
        if not DATE_RE.match(str(r.get("date", ""))):
            errors.append(f"{tag}: date 형식")
        kind = r.get("kind", "route")
        if kind not in KINDS:
            errors.append(f"{tag}: kind {kind!r} 는 허용 목록 밖")
        unknown = set(r) - KNOWN_FIELDS
        if unknown:
            warns.append(f"{tag}: 알 수 없는 필드 {sorted(unknown)} — 다음 버전에서 거절")
        if kind in NEEDS_INTAKE:
            ii = r.get("intake") or []
            if not ii:
                errors.append(f"{tag}: intake[] 비었다")
            for i in ii:
                if i not in intake_ids:
                    errors.append(f"{tag}: intake {i} 실재 안 함")
        claim = str(r.get("claim", ""))
        if not claim.strip():
            errors.append(f"{tag}: claim 비었다")
        elif not HANGUL.search(claim):
            errors.append(f"{tag}: claim 에 한국어가 없다 (재등장 대조는 grep 이다 · 영어 원문은 intake text 에)")
        if kind in {"route", "observation", "judgment"} and not re.search(r"[①②③④]", str(r.get("grade", ""))):
            errors.append(f"{tag}: grade 에 ①~④ 없음")
        if kind in NEEDS_THREE:
            for k in ("priced_in", "variant", "breaks_if"):
                if not str(r.get(k, "")).strip():
                    errors.append(f"{tag}: {k} 비었다 (observation/judgment 3행 필수)")
        # routed[] / parked
        routed = r.get("routed") or []
        if not isinstance(routed, list):
            errors.append(f"{tag}: routed 는 배열")
            routed = []
        hit_theses = []
        for x in routed:
            if not isinstance(x, str):
                errors.append(f"{tag}: routed 원소가 문자열 아님")
                continue
            if "#" in x:
                pg, t = x.split("#", 1)
                if pg in tid and t in tid[pg]:
                    hit_theses.append((pg, t))
                else:
                    errors.append(f"{tag}: routed {x!r} — 실재하는 page#T 아님")
            elif x in T:
                pass
            elif x.startswith("intake/") or x.startswith("events:"):
                errors.append(f"{tag}: routed {x!r} — intake 경로·소프트 타깃은 routed[] 에 넣지 않는다(parked 로)")
            else:
                errors.append(f"{tag}: routed {x!r} — 실재 페이지 아님")
        parked = r.get("parked")
        hit_entities = []
        if parked:
            for p in str(parked).split("|"):
                p = p.strip()
                if p in PARKED:
                    continue
                if p.startswith(ENTITY_PREFIX):
                    key = p[len(ENTITY_PREFIX):]
                    if key in ENT:
                        hit_entities.append(key)
                    else:
                        errors.append(f"{tag}: parked {p!r} — entities.companies 에 {key!r} 카드가 없다 "
                                      f"(같은 커밋에서 status:\"후보\" 카드를 만들고 watch[] 에 쌓는다)")
                    continue
                errors.append(f"{tag}: parked 값 {p!r} 허용 밖 {sorted(PARKED)} 또는 entity:<KEY>")
        action = str(r.get("action", ""))
        if kind in {"route", "observation", "judgment"}:
            if not routed and not parked:
                errors.append(f"{tag}: routed[] 도 parked 도 없다 — 테제에 안 닿는 줄은 routing 이 아니다 "
                              f"(회사·테마가 보이면 parked:\"entity:<KEY>\" + watch[] · 아니면 intake routed:\"skip:no-thesis\")")
            if "digest-only" in action and not hit_theses and not hit_entities:
                errors.append(f"{tag}: action digest-only 인데 테제도 엔티티 watch 도 건드리지 않았다 — "
                              f"브레인에 남지 않는 줄은 routing 이 아니다(parked:\"entity:<KEY>\" 로 쌓거나 skip)")
        # 엔티티 접촉 — parked entity:KEY 면 그 카드의 watch[] 에 이 줄이 있어야 한다(테제 접촉과 같은 원리)
        for key in hit_entities:
            watch = ENT[key].get("watch") or []
            if any(w.get("rid") == rid for w in watch):
                touched_ok += 1
                bad = [w for w in watch if w.get("rid") == rid and not HANGUL.search(str(w.get("one", "")))]
                if bad:
                    errors.append(f"{tag}: entities[{key}].watch 의 one 에 한국어가 없다")
            else:
                errors.append(f"{tag}: parked entity:{key} 인데 그 카드 watch[] 에 rid=={rid} 항목이 없다 — 쌓지 않은 관측은 routing 이 아니다")
            touched_total += 1
            if len(watch) > WATCH_SOFT_CAP:
                warns.append(f"entities[{key}].watch {len(watch)}줄 — 테제로 승격하거나 접을 때다(상한 {WATCH_SOFT_CAP})")
        # 테제 접촉 — routed 에 page#T 가 있으면 그 테제가 이 줄로 움직였어야 한다
        for pg, t in hit_theses:
            touched_total += 1
            th = tid[pg][t]
            in_log = any(e.get("rid") == rid for e in th.get("log", []) or [])
            in_ev = rid in (th.get("evidence") or [])
            fresh = str(th.get("last_tested", "")) >= str(r.get("date", ""))
            if in_log or (in_ev and fresh):
                touched_ok += 1
            else:
                errors.append(f"{tag}: {pg}#{t} 를 routed 했지만 log[].rid 도 evidence 도 없다 — 테제를 건드리지 않은 라우팅은 해석이 아니다")
        # 채점 가능성
        if kind == "prediction" and not DATE_RE.match(str(r.get("resolve_by", ""))):
            errors.append(f"{tag}: prediction 은 resolve_by(YYYY-MM-DD) 필수")
        if kind == "judgment" and "ⓑ" in str(r.get("verdict", "")) and not DATE_RE.match(str(r.get("resolve_by", ""))):
            errors.append(f"{tag}: ⓑ 도전은 resolve_by 필수 — 언제 틀렸는지 알 수 있어야 한다")
        if kind == "verdict" and not str(r.get("event", "")).strip():
            warns.append(f"{tag}: verdict 에 event 필드 없음 — 어느 이벤트를 판정했나")
        if kind == "correction" and not r.get("corrects"):
            errors.append(f"{tag}: correction 은 corrects(r-id) 필수")

    # 2b. entities.json — watch[] 항목 형식 (rid 가 routing 에 실재해야 종합이 판정으로 되돌아갈 수 있다)
    rids = {r.get("id") for r in rows}
    for key, card in ENT.items():
        watch = card.get("watch") or []
        if not isinstance(watch, list):
            errors.append(f"entities[{key}].watch 는 배열")
            continue
        for w in watch:
            if str(w.get("date", "")) < eff and not all_rows:
                continue
            wt = f"entities[{key}].watch {w.get('rid') or '?'}"
            for k in ("date", "grade", "rid", "one"):
                if not str(w.get(k, "")).strip():
                    errors.append(f"{wt}: {k} 비었다 (date·grade·rid·one 필수)")
            if w.get("rid") and w["rid"] not in rids:
                errors.append(f"{wt}: rid 가 routing.jsonl 에 없다")
            if not DATE_RE.match(str(w.get("date", ""))):
                errors.append(f"{wt}: date 형식")
        if card.get("status") == "후보" and not watch and not card.get("theses"):
            warns.append(f"entities[{key}] 후보 카드인데 watch 도 theses 도 없다 — 왜 있나")

    # 3. events.json — due 필드
    ev = json.load(io.open(EVENTS, encoding="utf-8")).get("events", [])
    today = date.today().isoformat()
    nodue = [e for e in ev if "due" not in e]
    if nodue:
        warns.append(f"events {len(nodue)}건에 due 없음 — 브리핑·감시가 건너뛴다 (when 이 날짜면 due 로 옮긴다)")
    for e in ev:
        d = e.get("due")
        if d is not None and not DATE_RE.match(str(d)):
            errors.append(f"events due {d!r} 형식 아님 (YYYY-MM-DD 또는 null): {str(e.get('what',''))[:40]}")
    past = [e for e in ev if e.get("due") and e["due"] < today]
    if past:
        warns.append(f"events 지난 이벤트 {len(past)}건 — 판정하고 지운다(§H1): "
                     + " · ".join(f"{e['due']} {str(e.get('what',''))[:30]}" for e in past[:4]))

    # 4. 통계
    legacy = len(rows) - len(new)
    print(f"[routing] 검사 {len(new)}줄 (effective {eff} · 레거시 {legacy}줄 제외) · 테제 접촉 {touched_ok}/{touched_total}")
    return report(errors, warns)


def report(errors, warns):
    for w in warns[:30]:
        print("[routing] ⚠ " + w)
    if errors:
        print(f"[routing] 🔴 거절 {len(errors)}건 — AGENTS.md §3")
        for e in errors[:40]:
            print("    · " + e)
        if len(errors) > 40:
            print(f"    … 외 {len(errors) - 40}건")
        return 1
    print("[routing] ✓ 계약 위반 없음")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
