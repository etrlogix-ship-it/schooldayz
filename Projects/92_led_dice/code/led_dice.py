#!/usr/bin/env python3
"""
LED Dice - Project 92
Roll a dice using 7 LEDs in the classic dice pattern.
Press button (or Enter) to roll!
"""

import time
import random

try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
    print("✅ Raspberry Pi detected!")
except ImportError:
    HARDWARE_MODE = False

# LED positions: TL=top-left, TR=top-right, ML=mid-left, C=centre,
#                MR=mid-right, BL=bot-left, BR=bot-right
LED_PINS = {
    "TL": 5,  "TR": 6,
    "ML": 13, "C": 19, "MR": 26,
    "BL": 21, "BR": 20
}
BUTTON_PIN = 17

# Which LEDs light up for each dice face
DICE_PATTERNS = {
    1: ["C"],
    2: ["TL", "BR"],
    3: ["TL", "C", "BR"],
    4: ["TL", "TR", "BL", "BR"],
    5: ["TL", "TR", "C", "BL", "BR"],
    6: ["TL", "TR", "ML", "MR", "BL", "BR"],
}

ASCII_DICE = {
    1: ["┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"],
    2: ["┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"],
    3: ["┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"],
    4: ["┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"],
    5: ["┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"],
    6: ["┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"],
}

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in LED_PINS.values():
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def set_leds(positions):
    """Turn on specific LED positions, turn off the rest."""
    for name, pin in LED_PINS.items():
        if HARDWARE_MODE:
            GPIO.output(pin, GPIO.HIGH if name in positions else GPIO.LOW)

def show_dice(number):
    """Display the dice in terminal."""
    print(f"\n  You rolled: {number}")
    for line in ASCII_DICE[number]:
        print(f"    {line}")

def roll_animation():
    """Show a rolling animation before the final result."""
    print("  🎲 Rolling", end="", flush=True)
    for _ in range(8):
        temp = random.randint(1, 6)
        if HARDWARE_MODE:
            set_leds(DICE_PATTERNS[temp])
        print(".", end="", flush=True)
        time.sleep(0.1 + _ * 0.03)  # gradually slow down
    print()

def main():
    print("=" * 40)
    print("  🎲 LED Dice - Raspberry Pi Project")
    print("=" * 40)

    if HARDWARE_MODE:
        setup()
        print("7 LEDs + button connected")
        print("Press button to roll!\n")
    else:
        print("Simulation mode — press Enter to roll!\n")

    total_rolls = 0
    roll_counts = {i: 0 for i in range(1, 7)}

    try:
        while True:
            if HARDWARE_MODE:
                print("  Waiting for button press...", end="\r")
                while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                    time.sleep(0.05)
                while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                    time.sleep(0.01)
            else:
                cmd = input("  Press Enter to roll (or 'q' to quit, 's' for stats): ").strip().lower()
                if cmd == 'q':
                    break
                if cmd == 's':
                    print(f"\n  📊 Roll statistics ({total_rolls} total):")
                    for n in range(1, 7):
                        bar = "█" * roll_counts[n]
                        pct = roll_counts[n]/total_rolls*100 if total_rolls else 0
                        print(f"  {n}: {bar:<20} {roll_counts[n]:3d} rolls ({pct:.0f}%)")
                    continue

            roll_animation()
            result = random.randint(1, 6)
            if HARDWARE_MODE:
                set_leds(DICE_PATTERNS[result])

            show_dice(result)
            total_rolls += 1
            roll_counts[result] += 1

            if HARDWARE_MODE:
                time.sleep(3)

    except KeyboardInterrupt:
        print("\n\n  Game over!")

    finally:
        if HARDWARE_MODE:
            set_leds([])
            GPIO.cleanup()

    if total_rolls > 0:
        print(f"\n  Total rolls: {total_rolls}")
        print(f"  Most common: {max(roll_counts, key=roll_counts.get)}")
    print("  Thanks for rolling! 🎲")

if __name__ == "__main__":
    main()
