import time
import threading

running = False
start_time = None
laps = []
elapsed = 0

def input_listener():
    global running, start_time, elapsed, laps
    while True:
        cmd = input().lower().strip()
        if cmd == "" :
            if not running:
                running = True
                start_time = time.time() - elapsed
                print("▶️  Started!")
            else:
                elapsed = time.time() - start_time
                running = False
                print(f"\n⏸️  Paused at {elapsed:.2f}s")
        elif cmd == "l":
            if running:
                lap_time = time.time() - start_time
                laps.append(lap_time)
                print(f"\n🏁 Lap {len(laps)}: {lap_time:.2f}s")
        elif cmd == "r":
            running = False
            start_time = None
            elapsed = 0
            laps = []
            print("\n🔄 Reset!")
        elif cmd == "q":
            print("\n👋 Goodbye!")
            import os; os._exit(0)

print("⏱️  Stopwatch")
print("=============")
print("Commands:")
print("  [Enter] = Start / Pause")
print("  l       = Lap")
print("  r       = Reset")
print("  q       = Quit\n")

t = threading.Thread(target=input_listener, daemon=True)
t.start()

while True:
    if running:
        current = time.time() - start_time
        mins, secs = divmod(current, 60)
        print(f"\r⏱️  {int(mins):02d}:{secs:05.2f}  (Enter=pause, l=lap, r=reset, q=quit)", end="", flush=True)
    time.sleep(0.05)
