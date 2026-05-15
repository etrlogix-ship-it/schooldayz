import time, json, os

FILE = "lyrics.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return {}
def save(s):
    with open(FILE,"w") as f: json.dump(s, f, indent=2)

songs = load()

def scroll_display(lyrics, delay=0.08):
    print()
    for line in lyrics.split("\n"):
        for char in line:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()
        time.sleep(0.2)

print("Song Lyric Display")
print("==================")
while True:
    print("\nCommands: add, display, list, quit")
    cmd = input("> ").strip().lower()
    if cmd == "add":
        title = input("Song title: ")
        artist = input("Artist: ")
        print("Enter lyrics (blank line to finish):")
        lines = []
        while True:
            line = input()
            if not line: break
            lines.append(line)
        songs[title.lower()] = {"title": title, "artist": artist,
                                 "lyrics": "\n".join(lines)}
        save(songs); print("Saved!")
    elif cmd == "display":
        if not songs:
            print("No songs saved!")
            continue
        print("Songs:", ", ".join(s["title"] for s in songs.values()))
        name = input("Which song? ").lower()
        if name in songs:
            s = songs[name]
            print(f"\n{s['title']} — {s['artist']}")
            scroll_display(s["lyrics"])
        else:
            print("Not found!")
    elif cmd == "list":
        for s in songs.values():
            print(f"  {s['title']} — {s['artist']}")
    elif cmd == "quit":
        break
