import time
import threading
import datetime

alarms = []

def check_alarms():
    while True:
        now = datetime.datetime.now()
        for alarm in alarms[:]:
            if now.hour == alarm["h"] and now.minute == alarm["m"] and now.second < 2:
                print(f"\n🔔 ALARM! {alarm['msg']}")
                print("\a" * 5)
                alarms.remove(alarm)
        time.sleep(1)

t = threading.Thread(target=check_alarms, daemon=True)
t.start()

print("Smart Alarm Clock")
print("=================")
print("Commands: set HH:MM <message>, list, delete <number>, quit")

while True:
    cmd = input("> ").strip().split(maxsplit=2)
    if not cmd: continue
    if cmd[0] == "set" and len(cmd) >= 2:
        try:
            h, m = map(int, cmd[1].split(":"))
            msg = cmd[2] if len(cmd) > 2 else "Wake up!"
            alarms.append({"h": h, "m": m, "msg": msg})
            print(f"Alarm set for {h:02d}:{m:02d} — {msg}")
        except (ValueError, IndexError):
            print("Usage: set HH:MM <message>")
    elif cmd[0] == "list":
        if alarms:
            for i, a in enumerate(alarms):
                print(f"  {i+1}. {a['h']:02d}:{a['m']:02d} — {a['msg']}")
        else:
            print("No alarms set.")
    elif cmd[0] == "delete" and len(cmd) > 1:
        try:
            idx = int(cmd[1]) - 1
            removed = alarms.pop(idx)
            print(f"Deleted alarm: {removed['msg']}")
        except (ValueError, IndexError):
            print("Invalid alarm number!")
    elif cmd[0] == "quit":
        break
    else:
        print("Commands: set HH:MM <msg>, list, delete <num>, quit")
