# TikTok Risk Control & For You Feed (FYP) Throttling Rules

> Last Verified: 2026-11-24

## 1. Enforcement Architecture & Shadowbanning (FYP Ineligibility)

- **Official Mechanism**: TikTok enforces "shadowbans" primarily as **For You Feed (FYP) ineligibility** and search suppression. Flagged videos remain on the creator's profile and visible to followers, but receive zero outward algorithmic distribution.
- **4-Tier Enforcement Ladder**: Progresses from account warnings and temporary feature restrictions to full account bans.
- **Cross-Account / Device Penalties**: Severe violations or ban-evasion attempts trigger automated penalties across associated accounts linked to the same device or network identity.
- **Appeals**: Creators can inspect flags in TikTok Studio / Analytics and appeal directly; winning an "unoriginal content" appeal usually requires original project files or unedited camera roll proof.

## 2. Unoriginal Content, Low-Quality Media & Off-Platform Redirects

TikTok aggressively suppresses content flagged as *"Not eligible for recommendation in the For You feed"*:
- **Third-Party Watermarks**: Re-uploading videos carrying visible watermarks or logos from Douyin, Instagram Reels, YouTube Shorts, CapCut, or Lemon8 triggers automatic FYP suppression.
- **QR Codes & Off-Platform Scanners**: Videos containing QR codes, barcodes, or explicit framing to pull users off-platform are heavily suppressed.
- **Static Images & Low-Effort Loops**: Videos built solely from static graphics, unedited slideshows without dynamic motion, heavy compression, GIFs, or ultra-short loops trigger low-quality throttling.
- **Unoriginal Re-Uploads & "AI Slop"**: Reposting clips, unedited podcast snippets, or mass-producing near-identical videos using the same AI template/avatar/prompt violates originality rules (especially strict for Creator Rewards Program and TikTok Shop affiliates). Content must show genuine human transformation, commentary, or unique editing.

## 3. AI-Generated Content (AIGC) Disclosure & C2PA Detection

- **Mandatory Disclosure Toggle**: Any video, image, or audio that uses AI to create or realistically alter people, voices, or scenes must enable the **"AI-generated content"** toggle prior to posting (or include clear on-screen disclosure).
- **Automated C2PA Detection**: TikTok reads C2PA Content Credentials and visual/audio patterns to auto-label or flag undisclosed synthetic media. Failing to disclose realistic AI content accelerates throttling or removal.
- **Strictly Prohibited AI Content (Even When Labeled)**:
  - Unauthorized deepfakes or voice clones of real individuals (including fake endorsements).
  - Inappropriate AI depictions of minors or private individuals.
  - Misleading synthetic media depicting real-world events or breaking news.

## 4. Commercial Disclosure & TikTok Shop Health (AHR / CHR)

- **Commercial Content Toggle**:
  - Brand sponsorships/partnerships must toggle **"Paid Partnership"**.
  - Self-promotion of a creator's own business/product must toggle **"Promotional content"**.
- **Account Health Rating (AHR) for Sellers & Creator Health Rating (CHR) for Affiliates**:
  - Rolling **0 to 1,000 point scale** evaluated over a **180-day window** (new accounts start at **200 points**).
  - **Green (200–1,000 pts)**: Healthy standing and normal distribution.
  - **Orange / Needs Improvement (51–199 pts, risk milestones near 150)**: Triggers milestone enforcements (7-, 14-, or 28-day restrictions on listings, campaigns, or affiliate commissions).
  - **Red (0–50 pts)**: Severe risk; hitting **0 points** results in permanent shop deactivation or loss of e-commerce privileges.
  - Unverified medical/wellness claims, deceptive product performance claims, or missing commercial/AI tags deduct CHR/AHR points.

## 5. Pre-Publish & Triage Checklist

1. Strip all third-party watermarks (CapCut, Reels, Douyin, Shorts) and avoid static slideshows or QR codes.
2. Enable **"AI-generated content"** if realistic synthetic visuals or cloned voices are present.
3. Enable **"Paid Partnership"** or **"Promotional content"** whenever a brand or product is promoted.
4. Ensure transformative human value-add (commentary, camera presence, custom editing) rather than templated batch output.
5. Check TikTok Studio Analytics for FYP ineligibility notices and appeal with raw footage if wrongly flagged.
