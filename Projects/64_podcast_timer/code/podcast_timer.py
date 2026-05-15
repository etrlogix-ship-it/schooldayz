import time, threading, datetime

running = False
start_time = None
markers = []

def timer_thread():
    while running:
        elapsed = time.time() - start_time
        mins, secs = divmod(int(elapsed), 60)
        print(f"\r🎙️  Recording: {mins:02d}:{secs:02d}  (m=marker, s=stop) ", end="", flush=True)
        time.sleep(0.5)

print("Podcast Recording Timer")
print("=======================")
print("Commands: start, stop, marker <note>, history, quit")

while True:
    cmd = input("\n> ").strip().split(maxsplit=1)
    if not cmd: continue
    if cmd[0] == "start" and not running:
        running = True
        start_time = time.time()
        t = threading.Thread(target=timer_thread, daemon=True)
        t.start()
        print("Recording started!")
    elif cmd[0] == "stop" and running:
        running = False
        elapsed = time.time() - start_time
        print(f"\nStopped! Total: {int(elapsed//60):02d}:{int(elapsed%60):02d}")
        if markers:
            print("Markers:")
            for m in markers: print(f"  {m}")
    elif cmd[0] == "marker" and running:
        elapsed = time.time() - start_time
        mins, secs = divmod(int(elapsed), 60)
        note = cmd[1] if len(cmd) > 1 else "marker"
        marker = f"[{mins:02d}:{secs:02d}] {note}"
        markers.append(marker)
        print(f"\nMarker: {marker}")
    elif cmd[0] == "history":
        for m in markers: print(f"  {m}")
    elif cmd[0] == "quit":
        running = False
        break
