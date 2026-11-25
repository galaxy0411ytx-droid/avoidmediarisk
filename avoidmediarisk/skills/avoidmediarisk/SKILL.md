---
name: avoidmediarisk
description: >-
  Analyze social media risk control (风控), algorithmic traffic throttling (限流),
  shadowbanning, AIGC disclosure, and commercial compliance across 7 platforms:
  Xiaohongshu (小红书), Douyin (抖音), WeChat Channels (微信视频号), TikTok, X (Twitter),
  Instagram, and YouTube. Use when auditing drafts before publishing, diagnosing
  sudden reach drops, checking off-platform redirect or prohibited-word risks, or
  syncing weekly platform policy updates.
license: MIT
metadata:
  version: "1.0.0"
---

# Avoid Media Risk (`avoidmediarisk`)

Audit content drafts, diagnose reach throttling, and maintain up-to-date platform risk control knowledge across:
**小红书 (`xiaohongshu`)**, **抖音 (`douyin`)**, **微信视频号 (`weixin-channels`)**, **TikTok (`tiktok`)**, **X (`x`)**, **Instagram (`instagram`)**, and **YouTube (`youtube`)**.

## Step 0: Weekly Freshness Check (7-Day Rule)

Before auditing or diagnosing, check whether the local platform references are current:

```bash
python3 ./scripts/check_freshness.py --platforms <platform_keys>
```

- The freshness threshold in [metadata.json](./references/metadata.json) is **7 days**.
- If the script exits with status `1` (`STALE`), **remind the user** that the platform rules are over 7 days old and offer (or run, if in sync mode) live web verification via `search_web` / `last30days` before proceeding.

## Select Workflow Mode

### Mode A: Pre-Publish Compliance Audit (发布前预审)

Use when the user provides a draft (title, body copy, spoken script, hashtags, visual/video description, links, or monetization plan) for one or more platforms.

1. **Fast offline pre-scan**:
   Run [precheck_text.py](./scripts/precheck_text.py) on the text:
   ```bash
   python3 ./scripts/precheck_text.py --text "<draft>" --platforms <platform_keys>
   ```
2. **Load only the relevant platform reference(s)** from `references/`:
   - 小红书: [xiaohongshu.md](./references/xiaohongshu.md)
   - 抖音: [douyin.md](./references/douyin.md)
   - 微信视频号: [weixin-channels.md](./references/weixin-channels.md)
   - TikTok: [tiktok.md](./references/tiktok.md)
   - X (Twitter): [x.md](./references/x.md)
   - Instagram: [instagram.md](./references/instagram.md)
   - YouTube: [youtube.md](./references/youtube.md)
3. **Evaluate across all 4 risk dimensions**:
   - **Content & Copy**: Prohibited/extreme claims, semantic variants, profanity placement, YMYL (medical/finance/legal) licensing gates, emotional/anxiety bait.
   - **Off-Platform Redirects & Commercialization**: Private-traffic redirect intent (WeChat/QR/variants), external URL penalties (X main body, YouTube Shorts disabled links), commercial disclosure (蒲公英报备, TikTok Paid Partnership/Promotional, Affiliate disclosures).
   - **AIGC & Originality**: Mandatory AI-content toggles/labels, C2PA/EXIF metadata rules, Instagram `AI-Generated Profile` vs. post edits, cross-platform watermarks (TikTok/CapCut/Reels/Douyin), low-effort template/"AI slop"/unoriginality filters.
   - **Account & Operational Behavior**: Device/IP multi-account switching, engagement pods, unofficial browser automation (X/IG), DM automation opt-in & 24h limits, account health score thresholds.
4. **Return a structured audit report per platform**:
   - **Blocking Redlines (阻断级红线)**: Must fix before publishing (likely removal, strike, or account penalty).
   - **Throttling Risks (限流/降权风险)**: Likely to suppress reach or recommendation eligibility.
   - **Required Platform Toggles (发布必填开关)**: e.g., AI disclosure toggle, commercial partnership tag, original-claim authorization.
   - **Safe Rewrites (合规改写建议)**: Concrete, ready-to-use copy/structural alternatives.

### Mode B: Shadowban & Throttling Diagnostics (限流排查)

Use when the user reports sudden impression drops, zero non-follower traffic, or warning notices.

1. Gather symptoms: platform, recent view/impression pattern (e.g., stuck at 100–200 views, "unable to promote/上热门", Account Status block, FYP ineligibility, yellow monetization icon), recent account actions, and whether AI/reused clips/links were used.
2. Read the target platform's reference file in `references/`.
3. Walk the platform's diagnostic checklist in priority order (Account Health/Status → Originality/Watermarks → AIGC Disclosure → Redirects/Links → Behavioral Automation) and provide concrete recovery steps.

### Mode C: Weekly Rule Learning & Sync (定期规则同步更新)

Use when triggered manually or by the weekly scheduled automation to learn new risk-control and throttling changes:

1. Run `python3 ./scripts/check_freshness.py` to inspect current dates.
2. For each platform, search recent official announcements and creator/developer community reports from the past 7–30 days (using `search_web` and `last30days` if available) covering:
   - Algorithm throttling & recommendation eligibility changes
   - AIGC / C2PA / synthetic media labeling updates
   - Commercial disclosure, off-platform link, and YMYL licensing rules
   - Account health scoring, spam/automation bans, and strike policies
3. Update only the affected files in `references/<platform>.md` with verified changes (preserving verified rules that have not changed).
4. Update `last_updated` dates in [metadata.json](./references/metadata.json) and prepend a concise dated entry to [changelog.md](./references/changelog.md).
5. Summarize what changed per platform (or confirm "No material policy changes detected") for the user.
