import json, os, datetime, random

FILE = "cars.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return []
def save(c):
    with open(FILE,"w") as f: json.dump(c, f, indent=2)

cars = load()
print("Car Spotter Log")
print("===============")
while True:
    print(f"\nPlates logged: {len(cars)}")
    print("Commands: log <plate>, list, stats, quit")
    cmd = input("> ").split(maxsplit=1)
    if not cmd: continue
    if cmd[0] == "log" and len(cmd) > 1:
        plate = cmd[1].upper().strip()
        cars.append({"plate": plate, "date": datetime.datetime.now().isoformat()})
        save(cars)
        print(f"Logged: {plate}")
    elif cmd[0] == "list":
        for c in cars[-20:]:
            print(f"  {c['plate']} — {c['date'][:10]}")
    elif cmd[0] == "stats":
        from collections import Counter
        plates = [c["plate"] for c in cars]
        print(f"\nTotal plates: {len(plates)}")
        print(f"Unique plates: {len(set(plates))}")
        if plates:
            counts = Counter(plates)
            print(f"Most spotted: {counts.most_common(1)[0][0]} ({counts.most_common(1)[0][1]} times)")
            starts = Counter(p[0] for p in plates)
            print(f"Most common starting letter: {starts.most_common(1)[0][0]}")
    elif cmd[0] == "quit":
        break
