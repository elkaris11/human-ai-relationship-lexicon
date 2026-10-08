from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
STOP = {"a", "an", "the", "and", "or", "to", "of", "in", "for", "with", "that", "is", "as", "by", "on", "from", "between"}

def normalize(value):
    return re.sub(r"[^a-z0-9]+", "", value.lower())

def tokens(value):
    return {word for word in re.findall(r"[a-z0-9]+", value.lower()) if word not in STOP and len(word) > 2}

def frontmatter(path):
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    pieces = text.split("---", 2)
    if len(pieces) < 3:
        return {}, text
    return yaml.safe_load(pieces[1]) or {}, pieces[2]
