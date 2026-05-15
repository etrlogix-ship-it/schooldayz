try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

import re

FEEDS = {
    "BBC News": "http://feeds.bbci.co.uk/news/rss.xml",
    "NASA":  "https://www.nasa.gov/rss/dyn/breaking_news.rss",
    "Science Daily": "https://www.sciencedaily.com/rss/all.xml",
}

def parse_rss(xml):
    items = []
    for item in xml.split("<item>")[1:8]:
        title = re.search(r"<title>(.*?)</title>", item, re.DOTALL)
        title = title.group(1).strip() if title else "No title"
        title = re.sub(r"<[^>]+>|<!\[CDATA\[|\]\]>", "", title).strip()
        items.append(title)
    return items

print("RSS News Feed Reader")
print("====================")
print("Feeds:", ", ".join(FEEDS.keys()))

while True:
    feed_name = input("\nChoose feed (or quit): ").strip()
    if feed_name.lower() == "quit": break
    
    feed_name_match = next((k for k in FEEDS if feed_name.lower() in k.lower()), None)
    if not feed_name_match:
        print("Feed not found!")
        continue
    
    if HAS_REQUESTS:
        try:
            r = requests.get(FEEDS[feed_name_match], timeout=10)
            items = parse_rss(r.text)
            print(f"\n=== {feed_name_match} ===")
            for i, item in enumerate(items, 1):
                print(f"  {i}. {item[:80]}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Install requests: pip3 install requests --break-system-packages")
