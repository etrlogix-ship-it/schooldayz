import time
import os

def clear(): os.system("clear")

def show_light(state):
    clear()
    print("=" * 20)
    print("   TRAFFIC LIGHT   ")
    print("=" * 20)
    lights = {"red": ("  [🔴]  ", "  [ ]  ", "  [ ]  "),
              "yellow": ("  [ ]  ", "  [🟡]  ", "  [ ]  "),
              "green": ("  [ ]  ", "  [ ]  ", "  [🟢]  ")}
    for line in lights[state]:
        print(line)
    print("=" * 20)
    print(f"  {state.upper()}")

sequence = [("red", 5), ("green", 4), ("yellow", 2)]
print("Traffic Light Simulator - Press Ctrl+C to stop")
time.sleep(1)

try:
    while True:
        for state, duration in sequence:
            show_light(state)
            time.sleep(duration)
except KeyboardInterrupt:
    print("\nTraffic light stopped!")
