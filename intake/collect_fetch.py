#!/usr/bin/env python3
"""주문형 URL 수집기 — 이 세션에서 egress 가 막힌 호스트를 GitHub Actions 러너에서 받아 intake/files/fetch/ 에 남긴다.

왜 있나(2026-09-20 · §H1 「새 예외의 기준은 편의가 아니라 실측 실패율」):
  아카이브 값의 등급이 ② 에서 안 올라가는 원인이 반복 측정됐다. 세션 샌드박스에서 막힌 호스트 —
  data.sec.gov · www.sec.gov · disclosures-clerk.house.gov · extapps2.oge.gov · eia.gov · FRED ·
  m.stock.naver.com · api.stock.naver.com · comp.wisereport.co.kr · www.korea.kr · 언론사 다수.
  이미 collect_sec.py(SEC)와 collect_congress.py(의회·OGE)를 워크플로로 우회했는데, 둘 다 <한 출처 전용>이라
  새 출처가 막힐 때마다 수집기를 하나씩 더 만들게 돼 있었다. 이 파일은 그 자리를 하나로 합친다.

무엇을 하지 않나:
  · 프록시를 우회하지 않는다. 세션의 egress 정책은 조직 정책이고 403/407 은 보고 대상이다(/root/.ccr/README.md).
    여기서 쓰는 것은 <사용자 소유 CI 러너의 정상 네트워크>다 — 이미 시세 봇·SEC·의회 수집기가 같은 길을 쓴다.
  · 판단하지 않는다. 원문 바이트만 남기고 파싱·비율·TTM 은 브레인 단계에서 한다(§R2).
  · https 만 받는다. 리다이렉트는 같은 스킴에서만 따라간다.

용법:
  python3 intake/collect_fetch.py                      # intake/requests/fetch_urls.txt 를 읽는다
  python3 intake/collect_fetch.py --url https://... --label naver_078350_fin

요청 파일 형식(한 줄 하나 · '#' 주석 · 빈 줄 무시):
  label | https://url            ← label 이 파일명이 된다(영숫자·._- 만)
  label | https://url | referer  ← 첨부 다운로드처럼 <어느 페이지에서 눌렀는지>를 따지는 곳에 쓴다
  https://url                    ← label 을 URL 에서 만든다
"""
import hashlib
import http.cookiejar
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import date

UA = "ourprochoi Research kenchoi@keywestaim.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "intake", "collected.jsonl")
REQ = os.path.join(ROOT, "intake", "requests", "fetch_urls.txt")
OUT = os.path.join(ROOT, "intake", "files", "fetch")
MAX_BYTES = 8 * 1024 * 1024  # 한 파일 8MB — 저장소가 수집 층 무게로 무너지지 않게

BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
# 호스트별 예외 — 왜(2026-09-20 실측): www.korea.kr 의 /common/download.do 는 식별 UA + 쿠키 없는 요청에
#   <응답을 끝내지 않는다>. 러너에서 10분 넘게 read 가 안 끝났고(run 35485990057) 세션에서는 relay 가 11초에 끊었다.
#   같은 호스트의 HTML(actuallyView.do)은 정상이므로 호스트 차단이 아니라 <첨부 엔드포인트 전용 조건>이다 —
#   브라우저 UA + 세션 쿠키(JSESSIONID) + Referer 를 붙인다.
#   ⚠ 기본 UA 는 바꾸지 않는다 — SEC 는 반대로 <식별 UA>를 요구한다(403). 호스트 화이트리스트로만 건다.
BROWSER_HOSTS = {"www.korea.kr"}
READ_DEADLINE = 120  # 초 · 벽시계. 찔끔찔끔 보내는 서버가 러너를 6시간 붙잡지 못하게 하는 상한

EXT = {"application/json": "json", "text/html": "html", "application/xhtml+xml": "html",
       "text/plain": "txt", "text/csv": "csv", "application/pdf": "pdf", "application/xml": "xml", "text/xml": "xml"}


def slug(s, n=60):
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s).strip("_")
    return (s[:n] or "url")


def label_from_url(url):
    m = re.match(r"https://([^/]+)(/[^?#]*)?", url)
    host = m.group(1) if m else "host"
    tail = (m.group(2) or "").rstrip("/").rsplit("/", 1)[-1] if m else ""
    return slug(f"{host}_{tail}" if tail else host)


def host_of(url):
    m = re.match(r"https://([^/]+)", url)
    return m.group(1) if m else ""


def read_capped(r):
    """MAX_BYTES 까지 읽되 벽시계 READ_DEADLINE 을 넘기면 끊는다.

    socket timeout 은 <한 번의 recv 가 조용한 시간>만 잰다 — 서버가 몇 초마다 몇 바이트씩 흘리면
    timeout 은 영원히 안 걸린다(2026-09-20 러너 실측). 전체 소요 시간에 상한을 따로 건다.
    """
    buf = bytearray()
    t0 = time.time()
    while len(buf) <= MAX_BYTES:
        if time.time() - t0 > READ_DEADLINE:
            raise TimeoutError(f"read deadline {READ_DEADLINE}s 초과 · {len(buf)}B 까지 받음")
        chunk = r.read(65536)
        if not chunk:
            break
        buf.extend(chunk)
    return bytes(buf)


def get(url, retries=3, timeout=45, referer=""):
    host = host_of(url)
    browserish = host in BROWSER_HOSTS
    last = "?"
    for i in range(retries):
        try:
            jar = http.cookiejar.CookieJar()
            opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
            hdrs = {
                "User-Agent": BROWSER_UA if browserish else UA,
                "Accept": "*/*",
                "Accept-Language": "ko,en;q=0.8",
                "Accept-Encoding": "gzip, deflate",
            }
            if browserish:
                hdrs["Referer"] = referer or f"https://{host}/"
                # 쿠키를 먼저 받아 둔다 — 첨부 엔드포인트는 세션 없이는 응답을 끝내지 않는다
                try:
                    warm = urllib.request.Request(referer or f"https://{host}/", headers=hdrs)
                    with opener.open(warm, timeout=timeout) as w:
                        w.read(1 << 20)
                except Exception:  # noqa: BLE001 — 워밍업 실패는 본 요청 결과로 판정한다
                    pass
            req = urllib.request.Request(url, headers=hdrs)
            with opener.open(req, timeout=timeout) as r:
                data = read_capped(r)
                if r.headers.get("Content-Encoding") == "gzip":
                    import gzip
                    try:
                        data = gzip.decompress(data)
                    except Exception:  # noqa: BLE001 — 잘린 gzip 은 그대로 남긴다
                        pass
                return r.status, (r.headers.get("Content-Type") or ""), data
        except urllib.error.HTTPError as e:
            # 4xx/5xx 는 재시도해도 같다 — 본문을 증거로 남기고 끝낸다
            return e.code, (e.headers.get("Content-Type") if e.headers else "") or "", e.read(65536)
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
            time.sleep(1.5 * (i + 1))
    return 0, "", last.encode()


def parse_requests(path):
    items = []
    if not os.path.exists(path):
        return items
    for ln in io.open(path, encoding="utf-8"):
        ln = ln.split("#", 1)[0].strip()
        if not ln:
            continue
        # label | url | referer  (뒤 둘은 생략 가능)
        parts = [x.strip() for x in ln.split("|")]
        if len(parts) == 1:
            lab, url, ref = "", parts[0], ""
        else:
            lab, url, ref = (parts + ["", ""])[:3]
        items.append((slug(lab) if lab else label_from_url(url), url, ref))
    return items


def main(argv):
    if "--url" in argv:
        url = argv[argv.index("--url") + 1]
        lab = argv[argv.index("--label") + 1] if "--label" in argv else label_from_url(url)
        ref = argv[argv.index("--referer") + 1] if "--referer" in argv else ""
        items = [(slug(lab), url, ref)]
    else:
        items = parse_requests(REQ)
    if not items:
        print(f"[fetch] 요청 없음 — {os.path.relpath(REQ, ROOT)} 가 비어 있다")
        return 0

    today = date.today().isoformat()
    day = os.path.join(OUT, today)
    os.makedirs(day, exist_ok=True)
    ids = set()
    if os.path.exists(LOG):
        for ln in io.open(LOG, encoding="utf-8"):
            if ln.strip():
                ids.add(json.loads(ln).get("id"))
    n, bad = 1, 0
    for lab, url, ref in items:
        rec = {"date": today, "kind": "fetch", "host": (re.match(r"https://([^/]+)", url) or [None, "?"])[1],
               "subject": lab, "auto": True, "routed": False, "url": url}
        while f"c-{today.replace('-', '')}-{n:02d}" in ids:
            n += 1
        rec["id"] = f"c-{today.replace('-', '')}-{n:02d}"
        ids.add(rec["id"])

        if not url.startswith("https://"):
            rec.update(status="skipped", note="https 만 받는다")
            bad += 1
        else:
            st, ctype, body = get(url, referer=ref)
            if ref:
                rec["referer"] = ref
            rec["content_type"] = ctype.split(";")[0].strip() or "—"
            if st != 200 or not body:
                rec.update(status=("blocked" if st in (0, 403, 407) else str(st)),
                           note=body[:200].decode("utf-8", "ignore"))
                bad += 1
            elif len(body) > MAX_BYTES:
                rec.update(status="too_big", bytes=len(body), note=f"{MAX_BYTES}B 상한 초과 — 저장하지 않음")
                bad += 1
            else:
                ext = EXT.get(rec["content_type"], "bin")
                if ext == "bin":
                    # 첨부 다운로드는 Content-Type 을 octet-stream 으로 주는 곳이 많다 — 매직으로 잡는다
                    if body[:4] == b"%PDF":
                        ext = "pdf"
                    elif body[:2] == b"PK" and url.lower().find("hwpx") >= 0:
                        ext = "hwpx"
                path = os.path.join(day, f"{lab}.{ext}")
                with open(path, "wb") as f:
                    f.write(body)
                rec.update(status="ok", file=os.path.relpath(path, ROOT), bytes=len(body),
                           sha256=hashlib.sha256(body).hexdigest()[:16])
            time.sleep(0.4)  # 같은 호스트 연타 방지
        io.open(LOG, "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"[fetch] {lab}: {rec['status']}" + (f" · {rec.get('bytes')}B · {rec.get('content_type')}"
                                                   if rec["status"] == "ok" else f" · {rec.get('note', '')[:120]}"))
    print(f"[fetch] {len(items) - bad}/{len(items)} 성공 → {os.path.relpath(day, ROOT)}")
    return 0  # 실패해도 워크플로를 막지 않는다 — 실패 자체가 collected.jsonl 에 status 로 남는다


if __name__ == "__main__":
    sys.exit(main(sys.argv))
