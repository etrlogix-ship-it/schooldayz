import time, os

print("Text Beat Maker!")
print("================")
print("Create beat patterns using: X (hit) . (rest) | (bar separator)")
print("Example: X.X. X.X. | X..X X..X")
print()

beats = {
    "kick": "X.X. X..X",
    "snare": "..X. ..X.",
    "hihat": "X.X. X.X.",
}

def play_beat(pattern, symbol="X", name="", bpm=120):
    beat_time = 60 / bpm / 4  # 16th note
    chars = pattern.replace("|", "").replace(" ", "")
    print(f"
{name:8}: ", end="")
    for char in chars:
        if char == symbol:
            print("█", end="", flush=True)
        else:
            print("·", end="", flush=True)
        time.sleep(beat_time)
    print()

while True:
    print("\nCommands: demo, custom, quit")
    cmd = input("> ").strip().lower()
    if cmd == "demo":
        try:
            bpm = int(input("BPM (60-200, default 120): ") or "120")
        except ValueError:
            bpm = 120
        print("\nPlaying beats (Ctrl+C to stop)...")
        try:
            while True:
                for name, pattern in beats.items():
                    play_beat(pattern, "X", name, bpm)
        except KeyboardInterrupt:
            print("\nStopped!")
    elif cmd == "custom":
        pattern = input("Enter your pattern (X = hit, . = rest, space ignored): ")
        bpm = 120
        play_beat(pattern.upper(), "X", "Custom", bpm)
    elif cmd == "quit":
        break
