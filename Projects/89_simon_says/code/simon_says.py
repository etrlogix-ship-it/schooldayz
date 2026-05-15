#!/usr/bin/env python3
"""
Simon Says - Project 89
Classic memory sequence game with 4 coloured LEDs and buttons.
Keyboard simulation mode for non-Pi computers.
"""

import time
import random
import sys

try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
    print("✅ Raspberry Pi detected!")
except ImportError:
    HARDWARE_MODE = False

# Hardware pin config
LEDS    = {"R": 17, "B": 18, "G": 27, "Y": 22}
BUTTONS = {"R":  5, "B":  6, "G": 13, "Y": 19}

COLOURS = ["R", "B", "G", "Y"]
NAMES   = {"R": "🔴 RED", "B": "🔵 BLUE", "G": "🟢 GREEN", "Y": "🟡 YELLOW"}
KEYS    = {"r": "R", "b": "B", "g": "G", "y": "Y"}

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for c in COLOURS:
        GPIO.setup(LEDS[c],    GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(BUTTONS[c], GPIO.IN,  pull_up_down=GPIO.PUD_UP)

def flash(colour, duration=0.4):
    """Flash one LED."""
    name = NAMES[colour]
    if HARDWARE_MODE:
        GPIO.output(LEDS[colour], GPIO.HIGH)
    print(f"  ▶ {name}  ●", end="\r", flush=True)
    time.sleep(duration)
    if HARDWARE_MODE:
        GPIO.output(LEDS[colour], GPIO.LOW)
    print(f"    {name}  ○", end="\r", flush=True)
    time.sleep(0.1)

def all_flash(times=2):
    """Flash all LEDs together (game over / start signal)."""
    for _ in range(times):
        for c in COLOURS:
            if HARDWARE_MODE:
                GPIO.output(LEDS[c], GPIO.HIGH)
        print("  💥 ALL LIGHTS  ████", end="\r", flush=True)
        time.sleep(0.3)
        for c in COLOURS:
            if HARDWARE_MODE:
                GPIO.output(LEDS[c], GPIO.LOW)
        time.sleep(0.2)

def show_sequence(sequence, speed=0.4):
    """Play the sequence to the player."""
    print(f"\n  👀 Watch carefully! ({len(sequence)} steps)")
    time.sleep(0.5)
    for c in sequence:
        flash(c, speed)
        time.sleep(0.05)
    print()

def get_hardware_input():
    """Wait for a button press, return the colour."""
    while True:
        for c in COLOURS:
            if GPIO.input(BUTTONS[c]) == GPIO.LOW:
                flash(c, 0.3)
                while GPIO.input(BUTTONS[c]) == GPIO.LOW:
                    time.sleep(0.01)
                return c
        time.sleep(0.01)

def get_keyboard_input():
    """Get input from keyboard (R/B/G/Y)."""
    print(f"  Your input (r=Red, b=Blue, g=Green, y=Yellow): ", end="", flush=True)
    while True:
        key = input().strip().lower()
        if key in KEYS:
            c = KEYS[key]
            flash(c, 0.2)
            return c
        print(f"  ❌ Press r, b, g, or y: ", end="", flush=True)

def get_player_sequence(length):
    """Collect the player's input sequence."""
    player_input = []
    print(f"\n  🕹️  Your turn! Repeat the sequence ({length} steps)")
    for i in range(length):
        print(f"  Step {i+1}/{length}: ", end="", flush=True)
        if HARDWARE_MODE:
            c = get_hardware_input()
        else:
            c = get_keyboard_input()
        player_input.append(c)
        print(f"  → {NAMES[c]}")
    return player_input

def main():
    print("=" * 45)
    print("  🎵 Simon Says - Raspberry Pi Project")
    print("=" * 45)

    if HARDWARE_MODE:
        setup()
        print("Hardware: 4 LEDs + 4 buttons")
    else:
        print("Simulation: use r/b/g/y keys + Enter")

    print("\n  Watch the sequence of coloured lights, then")
    print("  repeat it back in the same order.\n")
    print("  Press Enter to start...")
    input()

    high_score = 0
    play_again = True

    while play_again:
        sequence = []
        level = 0
        # How fast to show sequence (gets faster over time)
        base_speed = 0.5

        try:
            while True:
                level += 1
                # Add a random new colour to the sequence
                sequence.append(random.choice(COLOURS))

                speed = max(0.15, base_speed - (level * 0.02))
                print(f"\n{'='*45}")
                print(f"  Level {level}  |  Sequence length: {len(sequence)}")
                print(f"{'='*45}")

                # Show the sequence
                show_sequence(sequence, speed)

                # Get player input
                try:
                    player = get_player_sequence(len(sequence))
                except KeyboardInterrupt:
                    raise

                # Check answer
                if player == sequence:
                    print(f"\n  ✅ Correct! Well done!")
                    if level > high_score:
                        high_score = level
                    time.sleep(0.5)
                else:
                    # Find where they went wrong
                    for i, (expected, got) in enumerate(zip(sequence, player)):
                        if expected != got:
                            print(f"\n  ❌ Step {i+1}: Expected {NAMES[expected]}, got {NAMES[got]}")
                            break
                    all_flash(3)
                    print(f"\n  💀 GAME OVER! You reached level {level}")
                    print(f"  🏆 High score: {high_score}")
                    break

        except KeyboardInterrupt:
            print("\n\n⏹ Game stopped.")

        print("\n  Play again? (y/n): ", end="")
        try:
            again = input().strip().lower()
            play_again = again == 'y'
        except:
            play_again = False

    print(f"\n  Final high score: {high_score} levels")
    if HARDWARE_MODE:
        for c in COLOURS:
            GPIO.output(LEDS[c], GPIO.LOW)
        GPIO.cleanup()
    print("  Thanks for playing Simon Says! 🎵")

if __name__ == "__main__":
    main()
