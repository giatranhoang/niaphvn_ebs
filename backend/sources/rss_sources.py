import feedparser
from dateutil import parser as date_parser
import re

def fetch_rss(rss_url, source_name):
    feed = feedparser.parse(rss_url)
    items = []

    for entry in feed.entries:
        text = entry.get("summary", "")
        # Remove all HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        items.append({
            "source": source_name,
            "platform": "News",
            "title": entry.get("title", ""),
            "text": text,
            "published": parse_date(entry),
            "url": entry.get("link", "")
        })

    return items

def parse_date(entry):
    try:
        dt = date_parser.parse(entry.published)
        if dt.tzinfo:
            dt = dt.replace(tzinfo=None)  # Remove timezone, assume local time
        return dt
    except Exception:
        return None
