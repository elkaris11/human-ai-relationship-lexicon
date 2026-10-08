#!/usr/bin/env python3
import argparse
import re
import yaml
from common import ROOT, frontmatter

parser = argparse.ArgumentParser()
parser.add_argument("seedling")
parser.add_argument("--yes", action="store_true")
args = parser.parse_args()
seedlings = (ROOT / "thinkgarden/seedlings").resolve()
source = (seedlings / args.seedling).resolve()
if not source.exists() or source.parent != seedlings:
    raise SystemExit("Seedling not found.")
metadata, body = frontmatter(source)
term = metadata.get("term", source.stem)
slug = re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")
destination = ROOT / "lexicon/terms" / f"{slug}.md"
if destination.exists():
    raise SystemExit("Accepted term already exists.")
if not args.yes:
    raise SystemExit(f"Review complete? Re-run with --yes to promote {term}.")
metadata["status"] = "accepted"
content = "---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n"
content += body.replace("## Proposed definition", "## Definition")
content += "\n## History\n\nPromoted from the Thinkgarden after community and maintainer review.\n"
destination.write_text(content, encoding="utf-8")
source.unlink()
print(destination.relative_to(ROOT))
