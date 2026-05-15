try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
import random

fallback_quotes = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
    ("You are never too small to make a difference.", "Greta Thunberg"),
    ("Imagination is more important than knowledge.", "Albert Einstein"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
]

def get_quote():
    if HAS_REQUESTS:
        try:
            r = requests.get("https://zenquotes.io/api/random", timeout=5)
            data = r.json()[0]
            return data["q"], data["a"]
        except Exception:
            pass
    return random.choice(fallback_quotes)

print("Inspirational Quote of the Moment!")
print("===================================")
while True:
    quote, author = get_quote()
    print(f"\n\"{quote}\"")
    print(f"    — {author}")
    if input("\nAnother quote? (yes/no): ").lower() != "yes":
        break
print("Stay inspired!")
