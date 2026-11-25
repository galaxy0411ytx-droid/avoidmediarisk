# Rule Changelog

## 2026-11-24 (v1.0.0)
- Initial compilation of risk control, throttling, AIGC disclosure, off-platform redirect, and account health rules across 7 platforms:
  - 小红书 (Xiaohongshu): CES weights, stock note retro-auditing, Pugongying commercial disclosure, mandatory AIGC tagging, medical/finance professional licensing.
  - 抖音 (Douyin): Account Health Score (0–100/120 tiers), dual-track AIGC disclosure (badge + C2PA/EXIF), ASR voice moderation, subject liability, finance/medical certification gates.
  - 微信视频号 (WeChat Channels): Intent-based off-platform redirect enforcement, "unable to promote" shadowban diagnostic, authorized multi-platform original claims, AIGC badge.
  - TikTok: For You Feed (FYP) ineligibility rules (QR codes, static images, third-party watermarks, unoriginal AI slop), C2PA/AIGC disclosure, Commercial Content Disclosure, Shop AHR/CHR (0–1000).
  - X (Twitter): External link reach suppression & link-in-reply pattern, negative feedback weights (blocks/mutes/reports), SimClusters topical consistency, API vs. browser-automation enforcement.
  - Instagram: Recommendation Eligibility & Account Status diagnostics, Reels watermark suppression, AI-Generated Profile toggle vs. post edits, engagement bait & ManyChat 24h opt-in guardrails.
  - YouTube: Inauthentic Content policy (replacing repetitious content), Shorts clickable link restrictions, synthetic content disclosure, 90-day policy training for warnings, profanity monetization rules.
