import json, os, datetime

FILE = "notes.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return []
def save(n):
    with open(FILE,"w") as f: json.dump(n, f, indent=2)

notes = load()
print("Note Taking App")
print("===============")
while True:
    print(f"\n{len(notes)} notes | Commands: new, list, view <n>, delete <n>, search <word>, quit")
    cmd = input("> ").split(maxsplit=1)
    if not cmd: continue
    if cmd[0] == "new":
        title = input("Title: ").strip()
        text = input("Note: ").strip()
        notes.append({"title": title, "text": text,
                       "date": datetime.date.today().isoformat()})
        save(notes); print("Note saved!")
    elif cmd[0] == "list":
        for i, n in enumerate(notes):
            print(f"  {i+1}. [{n['date']}] {n['title']}")
    elif cmd[0] == "view" and len(cmd) > 1:
        try:
            n = notes[int(cmd[1])-1]
            print(f"\n[{n['date']}] {n['title']}\n{n['text']}")
        except (ValueError, IndexError): print("Invalid!")
    elif cmd[0] == "delete" and len(cmd) > 1:
        try:
            removed = notes.pop(int(cmd[1])-1)
            save(notes); print(f"Deleted: {removed['title']}")
        except (ValueError, IndexError): print("Invalid!")
    elif cmd[0] == "search" and len(cmd) > 1:
        q = cmd[1].lower()
        found = [n for n in notes if q in n["title"].lower() or q in n["text"].lower()]
        print(f"Found {len(found)}:")
        for n in found: print(f"  {n['title']}: {n['text'][:50]}")
    elif cmd[0] == "quit":
        break
