# Anthropic blog fragment — distillation defenses

- url: https://www.anthropic.com/research/distillation-defenses
- date on page: Oct 12, 2026
- opened: 2026-10-13 (WebFetch). Telegram Samsung_Global_AI_SW/4767 cites this URL.

Early evidence: methods reduced data harvested by distillers by around 90 to 99 percent. After the classifier, reasoning tokens extracted on Anthropic's own platform were consistently 10 to 100 times lower.

SWE-bench Verified, pretrained Claude trained on Claude Opus 4.8 transcripts: full transcripts 80.4%, summarized transcripts 71.8%.

Two-stage classifier false positive rate less than 0.1%. Tens of thousands of accounts banned, often in less than two hours. Since September 24, charging for some blocked requests. Turned away trillions of tokens of paying traffic.

Caveat in the post: do not yet know how long the gains last; have yet to see a highly sophisticated persistent circumvention; distillers spread traffic across third-party clouds and other inference platforms. Zhipu GLM-5.3 tried Claude Fable 5 then switched. Moonshot Kimi requests forwarded to Claude, including one the company believes was PLA-affiliated CCTV analysis.
