#!/usr/bin/env python3
import argparse
import json
from difflib import SequenceMatcher
from common import ROOT, normalize, tokens, frontmatter

def existing():
    output = []
    for path in (ROOT / "lexicon/terms").glob("*.md"):
        metadata, body = frontmatter(path)
        definition = body.split("## Definition", 1)[-1].split("##", 1)[0].strip() if "## Definition" in body else body
        output.append({"term": metadata.get("term", path.stem), "definition": definition, "path": str(path.relative_to(ROOT))})
    return output

def analyze(term, definition):
    rows = []
    normalized_term = normalize(term)
    definition_tokens = tokens(definition)
    for item in existing():
        spelling = SequenceMatcher(None, normalized_term, normalize(item["term"])).ratio()
        other_tokens = tokens(item["definition"])
        union = definition_tokens | other_tokens
        overlap = len(definition_tokens & other_tokens) / len(union) if union else 0
        if spelling >= 0.55 or overlap >= 0.20:
            relation = "possible spelling variant" if spelling >= 0.78 else "possible semantic neighbor" if overlap >= 0.45 else "review overlap"
            rows.append({**item, "spelling_similarity": round(spelling, 3), "definition_overlap": round(overlap, 3), "advisory_relation": relation})
    return sorted(rows, key=lambda row: max(row["spelling_similarity"], row["definition_overlap"]), reverse=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--term", required=True)
    parser.add_argument("--definition", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = {"term": args.term, "decision": "human review required", "semantic_neighbor_candidates": analyze(args.term, args.definition)}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Analysis for {args.term}")
        for row in result["semantic_neighbor_candidates"]:
            print(f"- {row['term']}: spelling={row['spelling_similarity']}, definition={row['definition_overlap']} ({row['advisory_relation']})")
