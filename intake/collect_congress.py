#!/usr/bin/env python3
"""정치인 거래공시를 받아 intake/files/congress/ 에 남긴다 — 하원 PTR + 행정부 OGE 278-T.

수집 층의 주기 수집기. 세션 샌드박스는 disclosures-clerk.house.gov 가 프록시 403 이라
GitHub Actions(collect-congress.yml)에서 돈다. 판단은 하지 않는다 — 인덱스 행과 PDF·텍스트만 남긴다.

경로(키 없이 열린다):
  https://disclosures-clerk.house.gov/public_disc/financial-pdfs/{YEAR}FD.zip
    → {YEAR}FD.txt (탭 구분 인덱스: Prefix Last First Suffix FilingType StateDst Year FilingDate DocID)
    → https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{YEAR}/{DocID}.pdf

FilingType 'P' = Periodic Transaction Report. 감시 대상은 intake/requests/congress_members.txt.

행정부(대통령·지명직)는 다른 계통이다 — OGE Form 278-T(거래 단위) · 278e(연 1회).
  https://extapps2.oge.gov/201/Presiden.nsf/PAS+Index?OpenView → $FILE/*.pdf
  278-T 가 하원 PTR 에 대응하는 거래 공시다(2026: 트럼프 3,600건+ 1~3월 · $220M~750M ②).
  ⚠ 이 다리는 첫 실행 전까지 미검증이다 — Domino 뷰라 HTML 구조가 바뀌면 0건으로 떨어진다(상태만 남긴다).

용법: collect_congress.py [YEAR] [--all] [--oge] [--no-house]
"""
import io, json, os, re, sys, zipfile, urllib.request
from datetime import date, datetime

UA = "ourprochoi Research kenchoi@keywestaim.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "intake", "collected.jsonl")
OUT = os.path.join(ROOT, "intake", "files", "congress")
WATCH = os.path.join(ROOT, "intake", "requests", "congress_members.txt")
BASE = "https://disclosures-clerk.house.gov/public_disc"


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except Exception as e:
        return 0, str(e).encode()


def watched():
    if not os.path.exists(WATCH):
        return None
    names = set()
    for l in io.open(WATCH, encoding="utf-8"):
        l = l.split("#", 1)[0].strip()
        if l:
            names.add(l.upper())
    return names or None


def pdf_text(raw):
    """best-effort. pypdf 없으면 건너뛴다 — 없다고 수집을 실패시키지 않는다."""
    try:
        from pypdf import PdfReader
    except Exception:
        return None
    try:
        rd = PdfReader(io.BytesIO(raw))
        return "\n".join((p.extract_text() or "") for p in rd.pages).strip() or None
    except Exception:
        return None


def seen_docids():
    ids = set()
    if os.path.exists(LOG):
        for l in io.open(LOG, encoding="utf-8"):
            l = l.strip()
            if not l or '"congress"' not in l:
                continue
            try:
                d = json.loads(l)
            except Exception:
                continue
            if d.get("kind") == "congress" and d.get("doc_id"):
                ids.add(str(d["doc_id"]))
    return ids


def collect_oge(year, today, log):
    """OGE 대통령·지명직 공시(278-T·278e). Domino 뷰 → $FILE PDF 링크 추출. best-effort."""
    idx = "https://extapps2.oge.gov/201/Presiden.nsf/PAS+Index?OpenView&Count=2000"
    st, body = get(idx)
    base = "c-" + today.replace("-", "") + "-oge"
    if st != 200:
        rec = {"id": base + "0", "date": today, "kind": "congress", "source_kind": "oge",
               "host": "extapps2.oge.gov", "path": "/201/Presiden.nsf/PAS+Index",
               "subject": f"OGE 대통령·지명직 공시 인덱스 {year}", "grade_hint": "①",
               "status": "blocked" if st in (0, 403) else str(st),
               "note": body[:160].decode(errors="ignore"), "routed": False, "auto": True}
        log.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"[oge] 인덱스 실패 {st}")
        return
    html = body.decode("utf-8", "replace")
    # 09-20 1차 실행: 링크 0건. Domino 뷰가 프레임셋이거나 링크 형태가 다르다 —
    # 구조를 모르는 채 고칠 수 없으므로 표본을 로그에 남겨 다음 실행이 스스로 알려주게 한다.
    links = re.findall(r'href="?([^"\s>]*?\$FILE/[^"\s>]+?\.pdf)"?', html, re.I)
    if not links:
        frames = re.findall(r'(?:src|href)="([^"]+\.nsf[^"]*)"', html, re.I)[:12]
        log.write(json.dumps({"id": base + "probe", "date": today, "kind": "congress", "source_kind": "oge",
                              "host": "extapps2.oge.gov", "path": "/201/Presiden.nsf/PAS+Index",
                              "subject": "OGE 인덱스 구조 표본 — $FILE 링크 0건", "grade_hint": "진단",
                              "status": "no_links", "bytes": len(html), "title": (re.search(r"<title>(.*?)</title>", html, re.I | re.S) or [None, ""])[1][:120].strip(),
                              "frames": frames, "head": re.sub(r"\s+", " ", html[:900]),
                              "routed": False, "auto": True}, ensure_ascii=False) + "\n")
        print(f"[oge] $FILE 링크 0 · {len(html)}B · 프레임/링크 표본 {len(frames)}건을 로그에 남겼다")
        return
    want = [u for u in dict.fromkeys(links) if "trump" in u.lower() and year in u]
    known = seen_docids()
    os.makedirs(os.path.join(OUT, "oge", year), exist_ok=True)
    n = 0
    print(f"[oge] 링크 {len(links)} · 트럼프·{year} {len(want)}")
    for u in want:
        doc = u.rsplit("/", 1)[-1]
        if doc in known:
            continue
        n += 1
        st2, raw = get(u if u.startswith("http") else "https://extapps2.oge.gov" + u)
        rec = {"id": f"{base}{n}", "date": today, "kind": "congress", "source_kind": "oge",
               "host": "extapps2.oge.gov", "path": u, "doc_id": doc, "member": "Donald J. Trump",
               "subject": f"OGE {doc}", "grade_hint": "① 공시 원문", "routed": False, "auto": True}
        if st2 == 200:
            fp = os.path.join(OUT, "oge", year, doc)
            open(fp, "wb").write(raw)
            rec.update(status="ok", file=os.path.relpath(fp, ROOT), bytes=len(raw))
            t = pdf_text(raw)
            if t:
                tp = fp.rsplit(".", 1)[0] + ".txt"
                io.open(tp, "w", encoding="utf-8").write(t)
                rec["text_file"] = os.path.relpath(tp, ROOT)
                ds = sorted(set(re.findall(r"\b(\d{1,2}/\d{1,2}/20\d\d)\b", t)))
                if ds:
                    rec["tx_dates_raw"] = ds[:8]
        else:
            rec.update(status="blocked" if st2 in (0, 403) else str(st2))
        log.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"  · {doc} → {rec['status']}")


def main(argv):
    year = next((a for a in argv[1:] if re.fullmatch(r"20\d\d", a)), str(date.today().year))
    every = "--all" in argv
    names = None if every else watched()
    today = date.today().isoformat()
    os.makedirs(os.path.join(OUT, year), exist_ok=True)
    log = io.open(LOG, "a", encoding="utf-8")

    if "--oge" in argv:
        collect_oge(year, today, log)
        if "--no-house" in argv:
            log.close()
            return 0

    url = f"{BASE}/financial-pdfs/{year}FD.zip"
    st, body = get(url)
    if st != 200:
        rec = {"id": f"c-{today.replace('-','')}-cg0", "date": today, "kind": "congress", "host": "disclosures-clerk.house.gov",
               "path": f"/public_disc/financial-pdfs/{year}FD.zip", "subject": f"하원 공시 인덱스 {year}",
               "grade_hint": "①", "status": "blocked" if st in (0, 403) else str(st),
               "note": body[:160].decode(errors="ignore"), "routed": False, "auto": True}
        log.write(json.dumps(rec, ensure_ascii=False) + "\n")
        log.close()
        print(f"[congress] 인덱스 실패 {st}: {rec['note'][:80]}")
        return 1

    with zipfile.ZipFile(io.BytesIO(body)) as z:
        txt = z.read(next(n for n in z.namelist() if n.lower().endswith(".txt"))).decode("utf-8", "replace")
    rows, hdr = [], None
    for line in txt.splitlines():
        f = line.split("\t")
        if hdr is None:
            hdr = [c.strip() for c in f]
            continue
        if len(f) < len(hdr):
            continue
        rows.append(dict(zip(hdr, [c.strip() for c in f])))

    ptr = [r for r in rows if r.get("FilingType") == "P"]
    if names:
        ptr = [r for r in ptr if r.get("Last", "").upper() in names]
    known = seen_docids()
    new = [r for r in ptr if r.get("DocID") not in known]
    print(f"[congress] {year} 전체 {len(rows)} · PTR {len(ptr)}"
          + (f" (감시 {len(names)}명)" if names else "") + f" · 신규 {len(new)}")

    n = 0
    for r in sorted(new, key=lambda x: x.get("FilingDate", "")):
        doc, last = r.get("DocID"), r.get("Last", "")
        purl = f"{BASE}/ptr-pdfs/{year}/{doc}.pdf"
        n += 1
        rec = {"id": f"c-{today.replace('-','')}-cg{n}", "date": today, "kind": "congress",
               "host": "disclosures-clerk.house.gov", "path": f"/public_disc/ptr-pdfs/{year}/{doc}.pdf",
               "doc_id": doc, "member": f"{r.get('First','')} {last}".strip(), "filed": r.get("FilingDate"),
               "subject": f"PTR {r.get('First','')} {last} · 제출 {r.get('FilingDate')} · DocID {doc}",
               "grade_hint": "① 공시 원문", "routed": False, "auto": True}
        pst, praw = get(purl)
        if pst == 200:
            p = os.path.join(OUT, year, f"{doc}.pdf")
            open(p, "wb").write(praw)
            rec.update(status="ok", file=os.path.relpath(p, ROOT), bytes=len(praw))
            t = pdf_text(praw)
            if t:
                tp = os.path.join(OUT, year, f"{doc}.txt")
                io.open(tp, "w", encoding="utf-8").write(t)
                rec["text_file"] = os.path.relpath(tp, ROOT)
                # 체결일과 공시일은 다르다 — 본문에서 가장 이른 체결일을 뽑아 둔다(09-19 C2 재발 방지)
                ds = sorted(set(re.findall(r"\b(\d{1,2}/\d{1,2}/20\d\d)\b", t)))
                if ds:
                    rec["tx_dates_raw"] = ds[:8]
        else:
            rec.update(status="blocked" if pst in (0, 403) else str(pst), note=praw[:120].decode(errors="ignore"))
        log.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"  · {rec['subject']} → {rec['status']}")
    log.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
