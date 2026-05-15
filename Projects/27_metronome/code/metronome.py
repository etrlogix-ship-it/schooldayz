import time
import os
import threading

running = False
bpm = 120

def tick():
    while running:
        interval = 60.0 / bpm
        print("TICK!", end="", flush=True)
        os.system("python3 -c "import time; print('\a', end='', flush=True)"")
        time.sleep(interval)

print("Digital Metronome")
print("=================")
print("Commands: start, stop, bpm <number>, quit")

while True:
    cmd = input("> ").strip().lower().split()
    if not cmd: continue
    if cmd[0] == "start" and not running:
        running = True
        t = threading.Thread(target=tick, daemon=True)
        t.start()
        print(f"Metronome started at {bpm} BPM")
    elif cmd[0] == "stop":
        running = False
        print("Stopped.")
    elif cmd[0] == "bpm" and len(cmd) > 1:
        try:
            bpm = int(cmd[1])
            print(f"BPM set to {bpm}")
        except ValueError:
            print("Enter a number for BPM")
    elif cmd[0] == "quit":
        running = False
        break
