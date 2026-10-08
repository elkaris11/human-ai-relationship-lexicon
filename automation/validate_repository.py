#!/usr/bin/env python3
from common import ROOT, frontmatter

errors = []
required = ["term", "status", "category"]
for folder in [ROOT / "lexicon/terms", ROOT / "thinkgarden/seedlings"]:
    for path in folder.glob("*.md"):
        metadata, body = frontmatter(path)
        for key in required:
            if not metadata.get(key):
                errors.append(f"{path.relative_to(ROOT)}: missing {key}")
        required_sections = ["## Definition" if folder.name == "terms" else "## Proposed definition", "## Semantic Neighbors"]
        for section in required_sections:
            if section not in body:
                errors.append(f"{path.relative_to(ROOT)}: missing {section}")
if errors:
    print("\n".join("ERROR: " + error for error in errors))
    raise SystemExit(1)
print("Repository validation passed.")
