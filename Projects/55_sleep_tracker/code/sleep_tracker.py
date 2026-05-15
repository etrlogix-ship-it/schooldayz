import json, os, datetime

FILE = "sleep.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return []
def save(s):
    with open(FILE,"w") as f: json.dump(s, f, indent=2)

sleep_log = load()

def parse_time(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

print("Sleep Tracker")
print("=============")
while True:
    print("\nCommands: log, stats, list, quit")
    cmd = input("> ").strip().lower()
    if cmd == "log":
        date = input("Date (YYYY-MM-DD, Enter for today): ").strip()
        if not date: date = datetime.date.today().isoformat()
        bedtime = input("Bedtime (HH:MM, e.g. 22:30): ").strip()
        wake = input("Wake time (HH:MM, e.g. 07:00): ").strip()
        try:
            b = parse_time(bedtime)
            w = parse_time(wake)
            duration = (w - b) % (24*60)  # handle midnight crossing
            sleep_log.append({"date": date, "bedtime": bedtime,
                               "wake": wake, "minutes": duration})
            save(sleep_log)
            hours = duration // 60
            mins = duration % 60
            print(f"Logged! You slept for {hours}h {mins}m")
            if duration < 480: print("Tip: Kids need 8-10 hours of sleep!")
        except ValueError:
            print("Invalid time format!")
    elif cmd == "stats":
        if sleep_log:
            durations = [e["minutes"] for e in sleep_log]
            avg = sum(durations) / len(durations)
            print(f"\nSleep entries: {len(sleep_log)}")
            print(f"Average sleep: {int(avg//60)}h {int(avg%60)}m")
            print(f"Most sleep: {max(durations)//60}h {max(durations)%60}m")
            print(f"Least sleep: {min(durations)//60}h {min(durations)%60}m")
        else:
            print("No data yet!")
    elif cmd == "list":
        for e in sleep_log[-7:]:
            h, m = e["minutes"]//60, e["minutes"]%60
            print(f"  {e['date']}: {e['bedtime']} → {e['wake']} ({h}h {m}m)")
    elif cmd == "quit":
        break
