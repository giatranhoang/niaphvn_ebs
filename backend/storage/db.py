import sqlite3
from dateutil import parser as date_parser

DB_PATH = 'storage/nipah_monitor.db'

def create_table():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''CREATE TABLE IF NOT EXISTS rss_items (
        id INTEGER PRIMARY KEY,
        source TEXT,
        platform TEXT,
        title TEXT,
        text TEXT,
        published TEXT,
        url TEXT UNIQUE
    )''')
    conn.commit()
    conn.close()

def insert_items(items):
    conn = sqlite3.connect(DB_PATH)
    for item in items:
        published_str = item['published'].isoformat() if item['published'] else None
        try:
            conn.execute('INSERT OR IGNORE INTO rss_items (source, platform, title, text, published, url) VALUES (?, ?, ?, ?, ?, ?)',
                         (item['source'], item['platform'], item['title'], item['text'], published_str, item['url']))
        except sqlite3.IntegrityError:
            pass  # URL already exists
    conn.commit()
    conn.close()

def get_all_items():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT source, platform, title, text, published, url FROM rss_items WHERE published IS NOT NULL ORDER BY published DESC')
    rows = cursor.fetchall()
    conn.close()
    items = []
    for row in rows:
        item = dict(zip(['source', 'platform', 'title', 'text', 'published', 'url'], row))
        if item['published']:
            item['published'] = date_parser.parse(item['published'])
        else:
            item['published'] = None
        items.append(item)
    return items