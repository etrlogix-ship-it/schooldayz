import json, os, datetime

FILE = "chores.json"
today = datetime.date.today().isoformat()

def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return {"chores": [], "completions": {}}
def save(d):
    with open(FILE,"w") as f: json.dump(d, f, indent=2)

data = load()
chores = data["chores"]
completions = data["completions"]

def points():
    return sum(c["points"] for cid, c in zip(range(len(chores)), chores)
               if today in completions.get(str(cid), []))

print("Chore Chart")
print("===========")
while True:
    print(f"\nToday\'s Points: {points()}")
    print("Commands: add <chore> <points>, list, done <num>, history, quit")
    cmd = input("> ").strip().split(maxsplit=2)
    if not cmd: continue
    if cmd[0] == "add" and len(cmd) >= 3:
        try:
            pts = int(cmd[2])
            chores.append({"name": cmd[1], "points": pts})
            save(data); print(f"Added: {cmd[1]} ({pts} pts)")
        except ValueError: print("Points must be a number!")
    elif cmd[0] == "list":
        for i, c in enumerate(chores):
            done = today in completions.get(str(i), [])
            print(f"  {i+1}. {'✅' if done else '⬜'} {c['name']} ({c['points']} pts)")
    elif cmd[0] == "done" and len(cmd) > 1:
        try:
            idx = str(int(cmd[1])-1)
            if idx not in completions: completions[idx] = []
            if today not in completions[idx]:
                completions[idx].append(today)
                save(data)
                print(f"Done! +{chores[int(idx)]['points']} points!")
            else:
                print("Already done today!")
        except (ValueError, IndexError): print("Invalid!")
    elif cmd[0] == "quit":
        break
