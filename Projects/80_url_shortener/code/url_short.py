import json, os, random, string

FILE = "short_urls.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return {}
def save(d):
    with open(FILE,"w") as f: json.dump(d, f, indent=2)

urls = load()

def make_code():
    while True:
        code = "".join(random.choices(string.ascii_lowercase+string.digits, k=5))
        if code not in urls: return code

print("Mini URL Shortener")
print("==================")
while True:
    print("\nCommands: shorten <url>, expand <code>, list, quit")
    cmd = input("> ").strip().split(maxsplit=1)
    if not cmd: continue
    if cmd[0] == "shorten" and len(cmd) > 1:
        url = cmd[1].strip()
        # Check if already shortened
        existing = next((c for c, u in urls.items() if u == url), None)
        if existing:
            print(f"Already exists: pi.local/{existing}")
        else:
            code = make_code()
            urls[code] = url
            save(urls)
            print(f"Shortened! Use: pi.local/{code}")
    elif cmd[0] == "expand" and len(cmd) > 1:
        code = cmd[1].strip()
        if code in urls:
            print(f"→ {urls[code]}")
        else:
            print("Code not found!")
    elif cmd[0] == "list":
        for code, url in urls.items():
            print(f"  pi.local/{code} → {url[:60]}")
    elif cmd[0] == "quit": break
