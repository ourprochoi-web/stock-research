#!/usr/bin/env python3
"""Offline tests for the judgment ledger. No network."""
from __future__ import annotations

import unittest
from datetime import datetime, timezone

from ledger_common import (
    cluster_records,
    confirm_stats,
    directional_verdict,
    eval_price_break,
    forbidden_keys,
    last_completed_close,
    score_horizon,
    validate_row,
)


def rec(**kwargs):
    base = {"id": "c-1", "channel": "a", "text": "", "subject": "", "url": ""}
    base.update(kwargs)
    return base


class ClusterTest(unittest.TestCase):
    def test_telegram_repost_of_one_url_is_one_origin(self):
        url = "삼성 HBM https://www.hankyung.com/article/202610078441g"
        rows = [
            rec(id="c-a", channel="aether", text=url, url="https://t.me/aether/1"),
            rec(id="c-b", channel="other", text=url, url="https://t.me/other/2"),
            rec(id="c-c", channel=None, text="본문", url="https://www.hankyung.com/article/202610078441g"),
        ]
        out = cluster_records(rows)
        self.assertEqual(out["independent_n"], 1)
        self.assertEqual(out["origins"][0]["kind"], "url")
        self.assertEqual(out["origins"][0]["n_items"], 3)

    def test_equal_numbers_without_url_collapse(self):
        text = "매출 195.0조 영업이익 107.4조 OPM 55.1%"
        rows = [
            rec(id="c-1", channel="a", text=text, url="https://t.me/a/1", message_id=1),
            rec(id="c-2", channel="b", text=text, url="https://t.me/b/2", message_id=2),
        ]
        out = cluster_records(rows)
        self.assertEqual(out["independent_n"], 1)
        self.assertEqual(out["origins"][0]["kind"], "numeric")

    def test_analyst_note_with_extra_figures_stays_separate(self):
        wire = rec(id="w", channel="a", text="매출 195.0조 영업이익 107.4조", url="https://t.me/a/1", message_id=1)
        note = rec(
            id="n", channel="jpm",
            text="영업이익 107.4조 컨센서스 106조 JPM 102조 장비 한 분기",
            url="https://t.me/jpm/9", message_id=9,
        )
        out = cluster_records([wire, note])
        self.assertEqual(out["independent_n"], 2)

    def test_same_earnings_print_collapses_onto_the_filing(self):
        filing = rec(
            id="dart", channel="beluga",
            text="삼성전자 매출액 : 1,950,000억 영업익 : 1,074,000억 https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20261008800004",
            url="https://t.me/beluga/1",
        )
        review = rec(id="rev", channel="aether", text="삼성전자 매출액 195.0조 영업이익 107.4조 OPM 55.1%", url="https://t.me/aether/2", message_id=2)
        vague = rec(id="v", channel="insider", text="삼성전자 영업이익 107조나왔네요", url="https://t.me/insider/3", message_id=3)
        note = rec(id="note", channel="meritz", text="삼성전자 매출 195.0조 영업이익 107.4조 https://vo.la/mmkr8tc", url="https://t.me/meritz/4")
        out = cluster_records([filing, review, vague, note])
        self.assertEqual(out["independent_n"], 1)
        self.assertEqual(out["origins"][0]["kind"], "filing")
        self.assertIn("rcpNo=20261008800004", out["origins"][0]["key"])

    def test_two_publishers_stay_two(self):
        rows = [
            rec(id="h", text="https://www.hankyung.com/article/1", url="https://t.me/a/1"),
            rec(id="b", text="https://www.bloomberg.com/news/articles/abc", url="https://t.me/b/2"),
        ]
        self.assertEqual(cluster_records(rows)["independent_n"], 2)


class PriceRuleTest(unittest.TestCase):
    def test_us_intraday_bar_is_not_the_close(self):
        # 2026-10-08 14:30 UTC is 10:30 ET. The Oct 8 bar must not be used.
        now = datetime(2026, 10, 8, 14, 30, tzinfo=timezone.utc)
        series = [("20261007", 100.0), ("20261008", 101.5)]
        self.assertEqual(last_completed_close(series, "20261008", "US", now), ("20261007", 100.0))

    def test_us_after_close_uses_same_day(self):
        now = datetime(2026, 10, 8, 21, 0, tzinfo=timezone.utc)  # 17:00 EDT
        series = [("20261007", 100.0), ("20261008", 101.5)]
        self.assertEqual(last_completed_close(series, "20261008", "US", now), ("20261008", 101.5))

    def test_kr_after_close_uses_same_day(self):
        now = datetime(2026, 10, 8, 7, 0, tzinfo=timezone.utc)  # 16:00 KST
        series = [("20261008", 263000.0)]
        self.assertEqual(last_completed_close(series, "20261008", "KR", now), ("20261008", 263000.0))


class ScoreTest(unittest.TestCase):
    def test_sign_rules(self):
        self.assertEqual(directional_verdict("긍정", 0.01), "hit")
        self.assertEqual(directional_verdict("긍정", 0.0), "miss")
        self.assertEqual(directional_verdict("부정", -0.02), "hit")
        self.assertEqual(directional_verdict("부정", 0.02), "miss")
        self.assertEqual(directional_verdict("중립", 0.2), "no-call")
        self.assertEqual(directional_verdict("헤지", 0.2), "manual")

    def test_pending_before_horizon(self):
        out = score_horizon("긍정", "excess", 100, [("20261108", 110)], [("20261008", 100), ("20261108", 100)],
                            "2026-10-08", 30, "2026-10-20")
        self.assertEqual(out["status"], "pending")
        self.assertIsNone(out["ret"])

    def test_excess_after_horizon(self):
        stock = [("20261008", 100), ("20261107", 110)]
        bench = [("20261008", 200), ("20261107", 210)]
        out = score_horizon("긍정", "excess", 100, stock, bench, "2026-10-08", 30, "2026-11-08")
        self.assertEqual(out["status"], "scored")
        self.assertAlmostEqual(out["ret"], 0.10)
        self.assertAlmostEqual(out["bench_ret"], 0.05)
        self.assertAlmostEqual(out["excess"], 0.05)
        self.assertEqual(out["verdict"], "hit")

    def test_manual_mode_does_not_invent_a_hit(self):
        out = score_horizon("부정", "manual", 100, [("20261107", 50)], [("20261008", 100), ("20261107", 100)],
                            "2026-10-08", 30, "2026-11-08")
        self.assertEqual(out["verdict"], "manual")
        self.assertIsNone(out["ret"])

    def test_price_break_fires(self):
        series = [("20261008", 140.0)]
        cond = {"check": "price", "op": "lt", "threshold": 150, "text": "CDS"}
        self.assertEqual(eval_price_break(cond, series, "2026-10-08")["status"], "fired")
        cond["check"] = "manual"
        self.assertEqual(eval_price_break(cond, series, "2026-10-08")["status"], "manual")


class ValidateTest(unittest.TestCase):
    def test_forbidden_weight(self):
        self.assertIn("weight", forbidden_keys({"weight": 0.1, "stance": "긍정"}))

    def test_missing_routing_and_korean(self):
        row = {
            "id": "j-20261008-01",
            "routing_id": "r-20261008-99",
            "date": "2026-10-08",
            "ticker": "005930",
            "market": "KR",
            "stance": "긍정",
            "score_mode": "excess",
            "claim_ko": "한국어 문장",
            "ref": {"price": 1, "endpoint": "https://example.test"},
            "horizons": ["30d", "90d"],
            "breaks_if": [{"text": "조건", "check": "manual"}],
            "pages": [],
        }
        errors = validate_row(row, {"r-20261008-10"}, {})
        self.assertTrue(any("routing" in e for e in errors))


class StreakTest(unittest.TestCase):
    def test_trailing_confirms_stop_at_refute(self):
        thesis = {"log": [
            {"mark": "ⓐ"}, {"mark": "ⓐ"}, {"mark": "ⓑ"},
            {"mark": "ⓐ"}, {"mark": "ⓐ"}, {"mark": "ⓐ"},
        ]}
        stats = confirm_stats(thesis)
        self.assertEqual(stats["confirm_streak"], 3)
        self.assertEqual(stats["confirm"], 5)
        self.assertEqual(stats["refute"], 1)
        self.assertFalse(stats["priced_in_warning"])

    def test_warning_at_five(self):
        thesis = {"log": [{"mark": "ⓐ"}] * 5}
        self.assertTrue(confirm_stats(thesis)["priced_in_warning"])


if __name__ == "__main__":
    unittest.main()
