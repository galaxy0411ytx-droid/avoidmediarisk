#!/usr/bin/env python3
"""Check whether platform rule references in avoidmediarisk are stale."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import sys


def load_metadata(meta_path: Path) -> dict:
    """Load platform metadata JSON from disk."""
    with meta_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def evaluate_freshness(
    metadata: dict,
    today: dt.date,
    platforms: list[str] | None = None,
) -> dict:
    """Evaluate staleness for requested or all configured platforms."""
    threshold = int(metadata.get("freshness_threshold_days", 7))
    configured = metadata.get("platforms", {})
    selected = platforms or list(configured.keys())

    results = []
    stale_platforms = []
    missing_platforms = []

    for name in selected:
        entry = configured.get(name)
        if not entry:
            missing_platforms.append(name)
            continue

        last_updated_raw = entry.get("last_updated", "")
        try:
            last_updated = dt.date.fromisoformat(last_updated_raw)
        except ValueError:
            stale_platforms.append(name)
            results.append(
                {
                    "platform": name,
                    "last_updated": last_updated_raw or "invalid",
                    "age_days": None,
                    "stale": True,
                }
            )
            continue

        age_days = (today - last_updated).days
        is_stale = age_days >= threshold
        if is_stale:
            stale_platforms.append(name)

        results.append(
            {
                "platform": name,
                "file": entry.get("file"),
                "last_updated": last_updated_raw,
                "age_days": age_days,
                "stale": is_stale,
            }
        )

    return {
        "checked_date": today.isoformat(),
        "threshold_days": threshold,
        "needs_refresh": bool(stale_platforms or missing_platforms),
        "stale_platforms": stale_platforms,
        "missing_platforms": missing_platforms,
        "platforms": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check freshness of avoidmediarisk platform rule references."
    )
    parser.add_argument(
        "--platforms",
        nargs="*",
        help="Optional subset of platform keys to check.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON.",
    )
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parent.parent
    meta_path = skill_root / "references" / "metadata.json"
    if not meta_path.is_file():
        print(f"Error: metadata file not found at {meta_path}", file=sys.stderr)
        return 2

    metadata = load_metadata(meta_path)
    report = evaluate_freshness(metadata, dt.date.today(), args.platforms)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(
            f"Rule Freshness Check ({report['checked_date']}, "
            f"threshold: {report['threshold_days']} days)"
        )
        for item in report["platforms"]:
            status = "STALE" if item["stale"] else "FRESH"
            print(
                f"  - {item['platform']}: {status} "
                f"(last_updated={item['last_updated']}, age_days={item['age_days']})"
            )
        if report["missing_platforms"]:
            print(f"Missing platforms: {', '.join(report['missing_platforms'])}")
        if report["needs_refresh"]:
            print(
                "\nACTION NEEDED: One or more platform references are >= "
                f"{report['threshold_days']} days old. Run live web research "
                "and update references/ + metadata.json."
            )
        else:
            print("\nAll checked platform references are up to date.")

    return 1 if report["needs_refresh"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
