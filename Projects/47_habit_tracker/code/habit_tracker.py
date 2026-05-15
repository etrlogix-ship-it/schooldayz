import json, os, datetime

FILE = "habits.json"
today = datetime.date.today().isoformat()

def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return {}
def save(h):
    with open(FILE,"w") as f: json.dump(h, f, indent=2)

habits = load()

def get_streak(logs):
    streak = 0
    d = datetime.date.today()
    while d.isoformat() in logs:
        streak += 1
        d -= datetime.timedelta(days=1)
    return streak

print("Habit Tracker")
print("=============")
while True:
    print(f"\nToday: {today}")
    if habits:
        for name, h in habits.items():
            done_today = today in h["logs"]
            streak = get_streak(h["logs"])
            status = "DONE" if done_today else "not done"
            print(f"  {'✅' if done_today else '⬜'} {name} — streak: {streak} days [{status}]")
    else:
        print("  No habits yet. Add one!")
    print("\nCommands: add <habit>, done <habit>, list, quit")
    cmd = input("> ").strip().split(maxsplit=1)
    if not cmd: continue
    if cmd[0] == "add" and len(cmd) > 1:
        habits[cmd[1]] = {"logs": []}
        save(habits); print(f"Added habit: {cmd[1]}")
    elif cmd[0] == "done" and len(cmd) > 1:
        if cmd[1] in habits:
            if today not in habits[cmd[1]]["logs"]:
                habits[cmd[1]]["logs"].append(today)
                save(habits)
                streak = get_streak(habits[cmd[1]]["logs"])
                print(f"Great job! Streak: {streak} days!")
            else:
                print("Already done today!")
        else:
            print("Habit not found!")
    elif cmd[0] == "quit":
        break
