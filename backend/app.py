from flask import Flask, jsonify, request
from flask_cors import CORS
import concurrent.futures
from sources.rss_sources import fetch_rss
from processors.filter import is_nipah_related
from storage.db import create_table, insert_items, get_all_items

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

create_table()

RSS_SOURCES = [
    {
        "name": "Suc Khoe Doi Song",
        'url': "https://suckhoedoisong.vn/rss/dich-benh.rss"
    },
    {
        "name": "Tuoi Tre",
        'url': "https://tuoitre.vn/rss/suc-khoe.rss"
    },
    {
        "name": "VnExpress",
        'url': "https://vnexpress.net/rss/suc-khoe.rss"
    },
    {
        "name": "Thanh Nien",
        'url': "https://thanhnien.vn/rss/suc-khoe.rss"
    },
    {
        "name": "SGGP",
        'url': "https://www.sggp.org.vn/rss/ytesuckhoe-212.rss"
    },
    {
        "name": "Vietnamnet",
        'url': "https://vietnamnet.vn/rss/suc-khoe.rss"
    },
    {
        "name": "VOA Tieng Viet - Suc Khoe",
        "url": "https://www.voatiengviet.com/api/z-tyml-vomx-tperiu_"
    },
    {
        "name": "Dan Tri - Suc khoe",
        "url": "https://dantri.com.vn/rss/suc-khoe.rss"
    }
]

@app.route('/api/items', methods=['GET'])
def get_items():
    items = get_all_items()
    return jsonify(items)

@app.route('/api/fetch', methods=['POST'])
def fetch_data():
    all_items = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_rss, source['url'], source['name']) for source in RSS_SOURCES]
        for future in concurrent.futures.as_completed(futures):
            items = future.result()
            nipah_items = [item for item in items if is_nipah_related(item['title'] + ' ' + item['text'])]
            all_items.extend(nipah_items)
    
    insert_items(all_items)
    return jsonify({"message": f"Fetched and inserted {len(all_items)} Nipah-related items"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)