#!/usr/bin/env python3
"""Offline regex pre-scan for common social media risk-control triggers."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

RULES: list[dict[str, str]] = [
    {
        "category": "extreme_advertising_claim",
        "severity": "high",
        "platforms": "xiaohongshu,douyin,weixin-channels",
        "pattern": r"(全网最低|全网唯一|国家级|绝对有效|根治|包治|100%有效|顶级|首款|首发|zui好|最(?:好|佳|强|低|高|便宜))",
        "note": "Potential China Advertising Law extreme/absolute claim.",
    },
    {
        "category": "private_traffic_redirect",
        "severity": "blocking",
        "platforms": "xiaohongshu,douyin,weixin-channels",
        "pattern": r"(加[vV微威]|微\s*信|[vV][xX]|绿泡泡|薇信|扣扣|QQ群|私我领|看主页领|扫码进群|二维码|后台留联系方式|去某宝搜|移步.{0,6}搜)",
        "note": "Off-platform/private-traffic redirect trigger or variant.",
    },
    {
        "category": "inducement_engagement_bait",
        "severity": "medium",
        "platforms": "weixin-channels,instagram,x,youtube",
        "pattern": r"(不转不是|点赞抽大奖|转发抽|快叫.{0,6}来看|comment\s+['\"]?[A-Za-z0-9_]+['\"]?\s+(?:below|to get))",
        "note": "Potential engagement-bait / inducement trigger.",
    },
    {
        "category": "external_url",
        "severity": "medium",
        "platforms": "x,youtube,xiaohongshu,douyin,weixin-channels,tiktok",
        "pattern": r"(https?://\S+|www\.\S+)",
        "note": "External URL: throttled in X main posts, disabled in YouTube Shorts, restricted in CN platforms.",
    },
    {
        "category": "ymyl_medical_finance",
        "severity": "high",
        "platforms": "xiaohongshu,douyin,weixin-channels,tiktok,youtube",
        "pattern": r"(荐股|稳赚不赔|低风险高收益|债务重组|美白祛斑|防脱发|降血压|降血糖|排毒养颜|医疗器械)",
        "note": "High-stakes medical/finance claim; requires platform licensing/qualification & strict compliance.",
    },
]


def scan_text(text: str, target_platforms: set[str] | None = None) -> list[dict]:
    """Scan input text against offline risk patterns."""
    findings: list[dict] = []
    for rule in RULES:
        rule_platforms = set(rule["platforms"].split(","))
        if target_platforms and not (target_platforms & rule_platforms):
            continue

        matches = sorted(
            {
                m.group(0)
                for m in re.finditer(rule["pattern"], text, flags=re.IGNORECASE)
            }
        )
        if matches:
            findings.append(
                {
                    "category": rule["category"],
                    "severity": rule["severity"],
                    "platforms": sorted(
                        target_platforms & rule_platforms
                        if target_platforms
                        else rule_platforms
                    ),
                    "matches": matches,
                    "note": rule["note"],
                }
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Offline pre-scan of draft text for media risk triggers."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Inline text to scan.")
    source.add_argument("--file", help="Path to UTF-8 text file to scan.")
    parser.add_argument(
        "--platforms",
        nargs="*",
        help="Optional platform filter (e.g. xiaohongshu douyin x).",
    )
    parser.add_argument("--json", action="store_true", help="Output JSON.")
    args = parser.parse_args()

    if args.file:
        text_path = Path(args.file)
        if not text_path.is_file():
            print(f"Error: file not found: {text_path}", file=sys.stderr)
            return 2
        content = text_path.read_text(encoding="utf-8")
    else:
        content = args.text

    target_set = set(args.platforms) if args.platforms else None
    findings = scan_text(content, target_set)

    if args.json:
        print(json.dumps({"findings": findings}, ensure_ascii=False, indent=2))
    else:
        if not findings:
            print("No obvious offline regex triggers detected.")
        else:
            print(f"Detected {len(findings)} risk pattern group(s):")
            for item in findings:
                print(
                    f"  [{item['severity'].upper()}] {item['category']} "
                    f"({', '.join(item['platforms'])}): {', '.join(item['matches'])}"
                )
                print(f"      -> {item['note']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
