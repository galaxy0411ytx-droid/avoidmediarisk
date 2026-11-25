# X (Twitter) Risk Control, Visibility Filtering & Reach Rules

> Last Verified: 2026-11-24

## 1. Algorithmic Objective & Negative Feedback Weights

- **Dwell Time & Conversation Priority**: X's ranking model maximizes in-app dwell time and active conversation. Replies, reposts, and bookmarks carry significantly higher positive weights than passive likes.
- **Heavy Negative Feedback Multipliers**: Open-source ranking signals and visibility filtering apply steep negative weights when users **block, mute, or report** a post. Repeated negative feedback degrades an account's baseline distribution across all posts ("visibility filtering" / shadowban symptoms).
- **SimClusters & Topical Consistency**: X maps accounts to topical clusters (including Grok-based semantic analysis). Sudden off-niche posting or erratic topic switching weakens cluster confidence and reduces initial out-of-network distribution.

## 2. External Links & Out-of-Network Throttling

- **Outbound Link Penalty**: Posts containing external URLs in the primary post body suffer severe distribution drops (especially for non-Premium accounts and in the *For You* out-of-network feed).
- **Best-Practice Pattern ("Link in Reply")**:
  - Publish native text, native images/video, or native X Articles in the main post without an external URL.
  - Place the external URL in the **first self-reply** (still avoid spamming identical links across consecutive posts or multiple accounts).

## 3. Spam, Duplicate Content & Automation Rules

X enforces a strict split between official API workflows and unauthorized automation:
- **Permitted Automation**: Official API-integrated schedulers (e.g., Buffer, Typefully, X's native scheduler) operating within official rate limits. Automated bot accounts must display the **"automated"** profile label.
- **Instant Suspension / Heavy Throttling Triggers**:
  - **Unofficial Browser Automation / Scraping**: Using Puppeteer, Selenium, or unofficial web wrappers to script actions instead of the official API.
  - **Duplicate Text / Repetitive Links**: Posting identical copy or the exact same external URL repeatedly across accounts or consecutive tweets/replies.
  - **Mass Aggressive Actions & Engagement Pods**: Automated mass-following, keyword-based auto-liking/auto-replying, or coordinated engagement rings artificially boosting posts.

## 4. Pre-Publish & Triage Checklist

1. Remove external URLs from the main post body; move links to the first reply or convert content to native media/articles.
2. Avoid copy-pasting identical text, promotional hooks, or links across multiple posts or replies.
3. Ensure any scheduling or publishing tool uses the **official X API** rather than headless browser scripting.
4. Keep posts aligned with the account's core SimCluster topics and optimize for replies/bookmarks rather than hollow engagement bait.
5. Check for sudden drops in out-of-network impressions (a common symptom of negative feedback accumulation or spam-classifier flagging).
