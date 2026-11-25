# avoidmediarisk

Multi-platform social media **risk control (风控)**, **traffic throttling (限流)**, and **pre-publish compliance audit** skill & plugin for AI agents.

## Supported Platforms

- **小红书 (Xiaohongshu / RedNote)** — CES weights, private-traffic redirect detection, AIGC tagging, Pugongying commercial disclosure, professional vertical licensing (medical/finance).
- **抖音 (Douyin)** — Account Health Score (健康分), multi-modal deduplication, mandatory AIGC dual-track disclosure (explicit badge + C2PA/EXIF metadata), ASR voice-to-text moderation, subject liability.
- **微信视频号 (WeChat Channels)** — Intent-based private-redirect enforcement, inducement rules, originality & cross-platform authorization, AIGC labeling.
- **TikTok** — For You Feed (FYP) ineligibility triggers, QR code/static image suppression, watermark penalties, C2PA AIGC rules, Commercial Content Disclosure, Shop AHR/CHR (0–1000).
- **X (Twitter)** — External link reach penalty, negative feedback weights (blocks/mutes/reports), SimClusters topic consistency, official API vs. browser-automation bans.
- **Instagram** — Recommendation Eligibility & Account Status diagnostics, Reels watermark suppression, AI-Generated Profile vs. post labeling, engagement bait & ManyChat 24h opt-in rules.
- **YouTube** — Inauthentic Content policy (replacing repetitious content), Shorts clickable link restrictions, synthetic media disclosure, Community Guidelines 90-day policy training, profanity monetization rules.

## Installation

### Via `skills.sh` (Recommended for Claude Code, Cursor, Codex, Antigravity, etc.)

```bash
npx skills add <your-github-username>/avoidmediarisk
```

Install globally across all projects:

```bash
npx skills add <your-github-username>/avoidmediarisk -g
```

### As an Antigravity Plugin

Copy or clone this repository into your Antigravity plugins directory:

```bash
git clone https://github.com/<your-github-username>/avoidmediarisk.git ~/.gemini/config/plugins/avoidmediarisk
```

## Capabilities

1. **Pre-Publish Compliance Audit (发布前预审)** — Analyze scripts, captions, titles, hashtags, visuals, and links against target platforms and output `Blocking Redlines`, `Throttling Risks`, and `Safe Rewrites`.
2. **Shadowban / Throttling Diagnostics (限流排查)** — Systematic triage when impressions drop or recommendations stop.
3. **Weekly Rule Freshness Check (每周规则保鲜)** — Tracks per-platform `last_updated` dates in `references/metadata.json` with a 7-day threshold, prompting live web verification when stale.

## Repository Layout

```text
avoidmediarisk/
├── plugin.json
├── README.md
├── LICENSE
├── assets/logo.svg
└── skills/avoidmediarisk/
    ├── SKILL.md
    ├── references/
    │   ├── metadata.json
    │   ├── changelog.md
    │   ├── xiaohongshu.md
    │   ├── douyin.md
    │   ├── weixin-channels.md
    │   ├── tiktok.md
    │   ├── x.md
    │   ├── instagram.md
    │   └── youtube.md
    └── scripts/
        ├── check_freshness.py
        └── precheck_text.py
```
