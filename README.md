# avoidmediarisk
## Overview

**avoidmediarisk** is a cross-platform AI agent skill and plugin built for creators, growth teams, and operators who publish across **Xiaohongshu (小红书), Douyin (抖音), WeChat Channels (微信视频号), TikTok, X (Twitter), Instagram, and YouTube**.

Modern social platforms rarely rely on simple keyword blacklists anymore. Instead, they combine multimodal AI moderation, off-platform redirect intent detection, C2PA/metadata AIGC tracking, account health scoring, and silent recommendation-eligibility throttling ("shadowbanning"). **avoidmediarisk** turns these scattered, fast-changing rules into a structured, repeatable pre-publish audit and diagnostic workflow.

### What It Does

1. **Pre-Publish Compliance Audit**: Scans draft titles, captions, spoken scripts, hashtags, visual descriptions, and links across 4 core dimensions—*Content & Copy Redlines*, *Off-Platform Redirects & Commercial Disclosure*, *AIGC Labeling & Originality*, and *Account Behavior & Vertical Licensing*—and returns blocking redlines, throttling risks, required platform toggles, and safe rewrites.
2. **Shadowban & Throttling Diagnostics**: Provides step-by-step triage checklists when impressions stall or non-follower reach drops (such as Instagram Account Status blocks, TikTok FYP ineligibility, WeChat Channels "unable to promote" flags, or X out-of-network link suppression).
3. **Offline Fast Pre-Scan**: Includes a zero-dependency Python pre-check script (`scripts/precheck_text.py`) to catch extreme advertising claims, private-traffic redirect variants, engagement bait, external URLs, and high-stakes medical/finance terms before publishing.
4. **7-Day Rule Freshness Tracking**: Tracks per-platform verification dates in `references/metadata.json` (`scripts/check_freshness.py`) and prompts live web verification whenever rules are more than 7 days old.
