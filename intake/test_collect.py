#!/usr/bin/env python3
"""collect.py 회귀 테스트 (2026-10-21) — 거짓 404 재시도·제자리 교체·자정 넘김 수집일.
네트워크 없이 돈다: fetch 를 가짜로 바꾸고 LOG/FILES 를 임시 폴더로 돌린다.
용법: python3 intake/test_collect.py
"""
import io, json, os, sys, tempfile
from datetime import datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import collect as C  # noqa: E402

DAY = "2026-10-20"


def setup(rows):
    tmp = tempfile.mkdtemp()
    C.LOG = os.path.join(tmp, "collected.jsonl"); C.FILES = os.path.join(tmp, "files")
    io.open(C.LOG, "w", encoding="utf-8").write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    return tmp


def rows():
    return [json.loads(l) for l in io.open(C.LOG, encoding="utf-8") if l.strip()]


def test_stale_404_retried_in_place():
    other = {"id": "c-20261020-t01", "date": DAY, "kind": "telegram", "host": "t.me", "status": "ok"}
    stale = {"id": "c-20261020-01", "date": DAY, "kind": "뉴스레터", "host": "soonsal.com", "status": "404", "file": None, "routed": False, "note": "HTTP 404"}
    tail = {"id": "c-20261020-t02", "date": DAY, "kind": "telegram", "host": "t.me", "status": "ok"}
    setup([other, stale, tail])
    calls = []
    def fake(url, timeout=25):
        calls.append(url)
        return (200, b"<html>soonsal 1020</html>") if "soonsal" in url else (200, b"tsmc page")
    C.fetch = fake
    C.main(["collect.py", "--date", DAY, "--no-macro"])
    R = rows()
    assert any("soonsal" in u for u in calls), "404 행이 재시도되지 않음"
    assert [r["id"] for r in R][:3] == ["c-20261020-t01", "c-20261020-01", "c-20261020-t02"], "제자리 교체 아님"
    s = R[1]
    assert s["status"] == "ok" and s["file"] == "intake/files/soonsal/2026/1020.html" and s["retry_of"] == "404", s
    assert sum(1 for r in R if r["host"] == "soonsal.com") == 1, "soonsal 줄이 늘었음"
    assert os.path.exists(os.path.join(C.FILES, "soonsal/2026/1020.html"))
    print("ok  stale 404 → 재시도·같은 id 제자리 교체(줄 수 그대로)")


def test_still_failing_replaced_not_appended():
    stale = {"id": "c-20261020-01", "date": DAY, "kind": "뉴스레터", "host": "soonsal.com", "status": "404", "file": None, "routed": False, "note": "HTTP 404"}
    setup([stale])
    C.fetch = lambda url, timeout=25: (404, b"") if "soonsal" in url else (403, b"")
    C.main(["collect.py", "--date", DAY, "--no-macro"])
    R = rows()
    assert [r["id"] for r in R if r["host"] == "soonsal.com"] == ["c-20261020-01"], R
    assert R[0]["status"] == "404" and R[0]["retry_of"] == "404"
    print("ok  또 404 → 줄 추가 없이 같은 id 갱신")


def test_ok_row_skipped():
    okrow = {"id": "c-20261020-01", "date": DAY, "kind": "뉴스레터", "host": "soonsal.com", "status": "ok", "file": "intake/files/soonsal/2026/1020.html", "sha256": "x"}
    setup([okrow])
    hit = []
    C.fetch = lambda url, timeout=25: (hit.append(url), (403, b""))[1]
    C.main(["collect.py", "--date", DAY, "--no-macro"])
    assert not any("soonsal" in u for u in hit), "ok 행을 다시 받음"
    assert rows()[0] == okrow
    print("ok  ok 행은 건너뜀")


def test_collection_day():
    os.environ.pop("COLLECT_DATE", None)
    kst = C.KST
    assert str(C.collection_day([], datetime(2026, 10, 20, 0, 7, tzinfo=kst))) == "2026-10-19"
    assert str(C.collection_day([], datetime(2026, 10, 20, 16, 30, tzinfo=kst))) == "2026-10-20"
    os.environ["COLLECT_DATE"] = "2026-10-19"
    assert str(C.collection_day([], datetime(2026, 10, 20, 9, 0, tzinfo=kst))) == "2026-10-19"
    assert str(C.collection_day(["--date", "2026-10-18"])) == "2026-10-18"
    os.environ.pop("COLLECT_DATE")
    print("ok  수집일: --date > COLLECT_DATE > 06:00 KST 전이면 전날")


if __name__ == "__main__":
    test_stale_404_retried_in_place()
    test_still_failing_replaced_not_appended()
    test_ok_row_skipped()
    test_collection_day()
    print("all ok")
