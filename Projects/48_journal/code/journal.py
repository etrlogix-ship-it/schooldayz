import json, os, datetime

FILE = "journal.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return []
def save(j):
    with open(FILE,"w") as f: json.dump(j, f, indent=2)

journal = load()

print("Digital Journal")
print("===============")
while True:
    print(f"\nEntries: {len(journal)}")
    print("Commands: write, read <num>, list, search <word>, quit")
    cmd = input("> ").strip().split(maxsplit=1)
    if not cmd: continue
    if cmd[0] == "write":
        mood = input("How are you feeling? (great/good/okay/bad): ").strip()
        print("Write your entry (type END on a new line to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == "END": break
            lines.append(line)
        entry = {"date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                 "mood": mood, "text": "\n".join(lines)}
        journal.append(entry)
        save(journal)
        print("Entry saved!")
    elif cmd[0] == "list":
        for i, e in enumerate(journal):
            print(f"  {i+1}. [{e['date']}] Mood: {e['mood']} — {e['text'][:40]}...")
    elif cmd[0] == "read" and len(cmd) > 1:
        try:
            idx = int(cmd[1]) - 1
            e = journal[idx]
            print(f"\n[{e['date']}] Mood: {e['mood']}")
            print(e["text"])
        except (ValueError, IndexError):
            print("Invalid entry number!")
    elif cmd[0] == "search" and len(cmd) > 1:
        q = cmd[1].lower()
        results = [e for e in journal if q in e["text"].lower()]
        print(f"Found {len(results)} entries with '{q}':")
        for e in results:
            print(f"  [{e['date']}] {e['text'][:60]}...")
    elif cmd[0] == "quit":
        break
