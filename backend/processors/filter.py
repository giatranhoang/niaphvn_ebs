import re

NIPAH_KEYWORDS = [
    "nipah",
    "nipah virus",
    "nipah outbreak",
    "nipah encephalitis",
    "virus nipah"
]

def is_nipah_related(text: str) -> bool:
    if not text:
        return False

    text = text.lower()
    return any(kw in text for kw in NIPAH_KEYWORDS)
