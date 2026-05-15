import time
import os

def countdown(seconds):
    print("\n⏳ Countdown started!\n")
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏱️  {timer} remaining   ", end="", flush=True)
        time.sleep(1)
    print("\r🔔 TIME'S UP!           ")
    # Ring the terminal bell
    print('\a', end='', flush=True)

print("🕐 Raspberry Pi Countdown Timer")
print("================================")
try:
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    total = minutes * 60 + seconds
    if total <= 0:
        print("Please enter a time greater than 0!")
    else:
        countdown(total)
except ValueError:
    print("Please enter valid numbers!")
