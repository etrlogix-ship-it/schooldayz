try:
    import wikipediaapi
    HAS_WIKI = True
except ImportError:
    HAS_WIKI = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

def simple_wiki_search(topic):
    if not HAS_REQUESTS:
        return None
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(' ', '_')}"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data.get("extract", "No summary available.")
        return None
    except Exception:
        return None

print("Wikipedia Lookup")
print("================")
print("Ask me anything! I will look it up on Wikipedia.")

while True:
    topic = input("\nSearch topic (or quit): ").strip()
    if topic.lower() == "quit": break
    
    result = simple_wiki_search(topic)
    if result:
        words = result.split()
        print(f"\n{topic}")
        print("=" * len(topic))
        # Print first 80 words
        print(" ".join(words[:80]))
        if len(words) > 80:
            print("\n[...more on Wikipedia...]")
    else:
        print("Not found or no internet connection.")
        print("Tip: Try a different spelling or more specific term.")
