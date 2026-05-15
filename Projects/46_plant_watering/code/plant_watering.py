import json, os, datetime

FILE = "plants.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return {}
def save(p):
    with open(FILE,"w") as f: json.dump(p, f, indent=2)

plants = load()
today = datetime.date.today()

def check_plants():
    print("\n=== Plant Status ===")
    for name, p in plants.items():
        last = datetime.date.fromisoformat(p["last_watered"])
        days_ago = (today - last).days
        freq = p["frequency_days"]
        days_until = freq - days_ago
        if days_until <= 0:
            status = f"NEEDS WATER! ({-days_until} days overdue)"
        elif days_until == 1:
            status = "Water tomorrow"
        else:
            status = f"Water in {days_until} days"
        print(f"  {name}: {status} (every {freq} days)")

print("Plant Watering Reminder")
print("=======================")
check_plants()

while True:
    print("\nCommands: add, watered, status, remove, quit")
    cmd = input("> ").strip().lower()
    if cmd == "add":
        name = input("Plant name: ").strip()
        freq = int(input("Water every how many days? "))
        plants[name] = {"last_watered": today.isoformat(), "frequency_days": freq}
        save(plants); print(f"Added {name}!")
    elif cmd == "watered":
        name = input("Which plant? ").strip()
        if name in plants:
            plants[name]["last_watered"] = today.isoformat()
            save(plants); print(f"Watered {name} today!")
        else:
            print("Plant not found!")
    elif cmd == "status":
        check_plants()
    elif cmd == "remove":
        name = input("Plant to remove: ").strip()
        if name in plants:
            del plants[name]; save(plants); print("Removed!")
        else:
            print("Not found!")
    elif cmd == "quit":
        break
