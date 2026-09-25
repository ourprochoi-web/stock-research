#!/usr/bin/env python3
"""Telegram public-channel collector — scrape t.me/s/{handle} preview pages (no Bot API).

Why (2026-09-23): 텔레그램 공개 채널 글이 user.jsonl 수동 붙여넣기에 의존해 왔다.
  t.me/s/ 미리보기 HTML 은 로그인·Bot 토큰 없이 최근 글을 준다. GitHub Actions 러너에서
  받아 intake/files/telegram/ 스니펫 + collected.jsonl 한 줄로 남긴다(판단 금지 · §R2).
2026-09-26: 한 줄을 쓰기 전에 intake/triage.py 로 분류한다 — 주장이 있으면 routed:false(+candidates),
  없으면 routed:"skip:<이유>". 원문은 똑같이 남는다.

Whitelist: intake/requests/telegram_channels.txt  (handle | notes · # 주석 · 빈 줄 무시)

Usage:
  python3 intake/collect_telegram.py                  # whitelist 전체
  python3 intake/collect_telegram.py --channel meritz_research
  python3 intake/collect_telegram.py --dry-run --channel meritz_research
"""
from __future__ import annotations

import argparse
import gzip
import html as htmlmod
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from triage import apply as triage_apply  # noqa: E402 — 2026-09-26 트리아지(분류만 · 판단 없음 · intake/triage.py)

KST = timezone(timedelta(hours=9))
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "intake", "collected.jsonl")
REQ = os.path.join(ROOT, "intake", "requests", "telegram_channels.txt")
OUT = os.path.join(ROOT, "intake", "files", "telegram")
HANDLE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{3,64}$")


class TGPreviewParser(HTMLParser):
    """Parse t.me/s/ preview HTML into {handle, id, datetime, text}.

    Robust to minor class churn: a message is any div with data-post="handle/id";
    text is the first nested div whose class contains tgme_widget_message_text;
    datetime is the first <time datetime="..."> inside the message.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.posts = []
        self._in_msg = False
        self._msg_depth = 0
        self._cur = None
        self._in_text = False
        self._text_depth = 0
        self._text_parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        cls = ad.get("class", "") or ""
        classes = cls.split()
        if (
            tag == "div"
            and "data-post" in ad
            and ("js-widget_message" in classes or "tgme_widget_message" in classes)
        ):
            post = ad["data-post"]
            if "/" not in post:
                return
            handle, mid = post.split("/", 1)
            if not mid.isdigit():
                return
            self._in_msg = True
            self._msg_depth = 1
            self._cur = {"handle": handle, "id": mid, "datetime": None, "text": ""}
            self._text_parts = []
            self._in_text = False
            self._text_depth = 0
            return
        if not self._in_msg:
            return
        if tag == "div":
            self._msg_depth += 1
            if not self._in_text and "tgme_widget_message_text" in cls:
                self._in_text = True
                self._text_depth = 1
                return
            if self._in_text:
                self._text_depth += 1
        elif self._in_text and tag == "br":
            self._text_parts.append("\n")
        elif (
            tag == "time"
            and self._cur is not None
            and not self._cur["datetime"]
            and ad.get("datetime")
        ):
            self._cur["datetime"] = ad["datetime"]

    def handle_endtag(self, tag):
        if not self._in_msg:
            return
        if self._in_text and tag == "div":
            self._text_depth -= 1
            if self._text_depth <= 0:
                self._in_text = False
        if tag == "div":
            self._msg_depth -= 1
            if self._msg_depth <= 0 and self._cur is not None:
                text = "".join(self._text_parts)
                text = re.sub(r"[ \t]+\n", "\n", text)
                text = re.sub(r"\n{3,}", "\n\n", text).strip()
                self._cur["text"] = text
                self.posts.append(self._cur)
                self._in_msg = False
                self._cur = None
                self._text_parts = []

    def handle_data(self, data):
        if self._in_text:
            self._text_parts.append(data)


def now_kst():
    return datetime.now(KST)


def read_handles(path):
    handles = []
    if not os.path.exists(path):
        return handles
    for ln in io.open(path, encoding="utf-8"):
        ln = ln.split("#", 1)[0].strip()
        if not ln:
            continue
        handle = ln.split("|", 1)[0].strip().lstrip("@")
        if not handle:
            continue
        if not HANDLE_RE.match(handle):
            print(f"[telegram] skip invalid handle: {handle!r}")
            continue
        handles.append(handle)
    return handles


def fetch(url, retries=3, timeout=45):
    last = b"?"
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Language": "ko,en;q=0.8",
                "Accept-Encoding": "gzip, deflate",
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    try:
                        data = gzip.decompress(data)
                    except Exception:  # noqa: BLE001
                        pass
                return r.status, data
        except urllib.error.HTTPError as e:
            return e.code, e.read(65536) if e.fp else b""
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}".encode()
            time.sleep(1.5 * (i + 1))
    return 0, last


def parse_posts(html_bytes, expect_handle=None):
    html = html_bytes.decode("utf-8", "replace")
    # Fallback if Telegram wraps entities oddly
    p = TGPreviewParser()
    try:
        p.feed(html)
    except Exception as e:  # noqa: BLE001 — fall through to regex
        print(f"[telegram] HTMLParser failed ({e}); using regex fallback")
        p.posts = []
    posts = p.posts
    if not posts:
        posts = regex_fallback(html)
    out = []
    seen = set()
    for post in posts:
        if expect_handle and post["handle"].lower() != expect_handle.lower():
            continue
        key = post["id"]
        if key in seen:
            continue
        seen.add(key)
        out.append(post)
    return out


def regex_fallback(html):
    """Last-resort scrape if class names drift; still keyed on data-post + <time>."""
    posts = []
    for m in re.finditer(
        r'data-post="([A-Za-z][\w]{3,64})/(\d+)"([\s\S]*?)(?=data-post="|$)', html
    ):
        handle, mid, chunk = m.group(1), m.group(2), m.group(3)[:12000]
        dt_m = re.search(r'<time[^>]*datetime="([^"]+)"', chunk)
        tx_m = re.search(
            r'class="[^"]*tgme_widget_message_text[^"]*"[^>]*>([\s\S]*?)</div>', chunk
        )
        text = ""
        if tx_m:
            t = re.sub(r"<br\s*/?>", "\n", tx_m.group(1), flags=re.I)
            t = re.sub(r"<[^>]+>", "", t)
            text = htmlmod.unescape(t).strip()
        posts.append({
            "handle": handle,
            "id": mid,
            "datetime": dt_m.group(1) if dt_m else None,
            "text": text,
        })
    return posts


def load_existing_urls(path):
    urls = set()
    ids = set()
    if not os.path.exists(path):
        return urls, ids
    for ln in io.open(path, encoding="utf-8"):
        ln = ln.strip()
        if not ln:
            continue
        try:
            rec = json.loads(ln)
        except json.JSONDecodeError:
            continue
        u = rec.get("url")
        if u:
            urls.add(u)
        i = rec.get("id")
        if i:
            ids.add(i)
    return urls, ids


def post_day_kst(iso_dt):
    """Folder date = post datetime in KST; fall back to today KST."""
    if not iso_dt:
        return now_kst().date().isoformat()
    try:
        # Telegram serves +00:00 ISO
        dt = datetime.fromisoformat(iso_dt.replace("Z", "+00:00"))
        return dt.astimezone(KST).date().isoformat()
    except ValueError:
        return now_kst().date().isoformat()


def snippet(text, n=120):
    one = re.sub(r"\s+", " ", text).strip()
    if len(one) <= n:
        return one
    return one[: n - 1] + "…"


def next_id(today, ids, n):
    # Prefix 't' so concurrent collectors never collide (see collect_fetch.py note).
    day = today.replace("-", "")
    while f"c-{day}-t{n:02d}" in ids:
        n += 1
    return f"c-{day}-t{n:02d}", n + 1


def collect_channel(handle, existing_urls, ids, id_n, dry_run=False):
    url = f"https://t.me/s/{handle}"
    st, body = fetch(url)
    today = now_kst().date().isoformat()
    collected_at = now_kst().strftime("%Y-%m-%dT%H:%M:%S%z")
    # %+0900 -> +09:00
    if len(collected_at) >= 5 and collected_at[-5] in "+-" and collected_at[-3] != ":":
        collected_at = collected_at[:-2] + ":" + collected_at[-2:]

    if st != 200 or not body or not isinstance(body, (bytes, bytearray)):
        note = body[:200].decode("utf-8", "ignore") if isinstance(body, (bytes, bytearray)) else str(body)
        rec = {
            "id": None,
            "date": today,
            "kind": "telegram",
            "host": "t.me",
            "channel": handle,
            "subject": f"t.me/s/{handle} fetch failed",
            "status": "blocked" if st in (0, 403, 407) else str(st or "error"),
            "url": url,
            "collected_at": collected_at,
            "routed": False,
            "auto": True,
            "note": note,
        }
        rid, id_n = next_id(today, ids, id_n)
        rec["id"] = rid
        ids.add(rid)
        if not dry_run:
            io.open(LOG, "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"[telegram] {handle}: FAIL {rec['status']} · {note[:80]}")
        return 0, 0, id_n

    posts = parse_posts(body, expect_handle=handle)
    added = skipped = 0
    for post in posts:
        post_url = f"https://t.me/{handle}/{post['id']}"
        if post_url in existing_urls:
            skipped += 1
            continue
        text = post["text"] or ""
        day = post_day_kst(post.get("datetime"))
        rel_file = None
        if not dry_run:
            day_dir = os.path.join(OUT, handle, day)
            os.makedirs(day_dir, exist_ok=True)
            # Raw snippet: full post text (or placeholder for media-only)
            fname = f"{post['id']}.txt"
            fpath = os.path.join(day_dir, fname)
            payload = text if text else f"[no text · media-only]\n{post_url}\n"
            with io.open(fpath, "w", encoding="utf-8") as fh:
                fh.write(payload)
            rel_file = os.path.relpath(fpath, ROOT)

        rid, id_n = next_id(today, ids, id_n)
        ids.add(rid)
        existing_urls.add(post_url)
        subj = snippet(text) if text else f"(media-only) {handle}/{post['id']}"
        rec = {
            "id": rid,
            "date": today,
            "kind": "telegram",
            "host": "t.me",
            "channel": handle,
            "message_id": post["id"],
            "subject": subj,
            "text": text,
            "url": post_url,
            "posted_at": post.get("datetime"),
            "collected_at": collected_at,
            "status": "ok",
            "file": rel_file,
            "routed": False,
            "auto": True,
            "grade_hint": "②(공개 채널 미리보기 · 원문 미검증)",
        }
        # 2026-09-26: 수집 직후 트리아지 — 링크만·본문 없음·이름도 주장 신호도 없음 → routed:"skip:<이유>",
        #   주장이 있으면 routed:false + candidates(걸리는 테제 후보). 판단은 하지 않는다. 사흘간 501건이
        #   전부 false 로 들어와 큐가 456건이 된 것이 계기(intake/triage.py 머리글).
        triage_apply(rec)
        if not dry_run:
            io.open(LOG, "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
        added += 1
        print(f"[telegram] + {handle}/{post['id']} · {subj[:80]}")

    print(f"[telegram] {handle}: +{added} new · {skipped} dup · {len(posts)} on page")
    time.sleep(0.5)
    return added, skipped, id_n


def main(argv=None):
    ap = argparse.ArgumentParser(description="Collect public Telegram channel posts via t.me/s/")
    ap.add_argument("--channel", help="single handle (skip whitelist)")
    ap.add_argument("--dry-run", action="store_true", help="parse & print; do not write files/jsonl")
    args = ap.parse_args(argv)

    if args.channel:
        handles = [args.channel.lstrip("@")]
    else:
        handles = read_handles(REQ)
    if not handles:
        print(f"[telegram] no channels — {os.path.relpath(REQ, ROOT)} empty or missing")
        return 0

    existing_urls, ids = load_existing_urls(LOG)
    id_n = 1
    total_new = total_dup = 0
    for h in handles:
        a, s, id_n = collect_channel(h, existing_urls, ids, id_n, dry_run=args.dry_run)
        total_new += a
        total_dup += s
    mode = "dry-run" if args.dry_run else "wrote"
    print(f"[telegram] done · {mode} · +{total_new} new · {total_dup} dup · {len(handles)} channel(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
