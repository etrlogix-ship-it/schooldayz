#!/usr/bin/env python3
"""
Two-Player Reaction Timer - Project 94
Who has faster reflexes? Find out with this two-player reaction game!
"""

import time
import random
import threading

try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
except ImportError:
    HARDWARE_MODE = False

# Pins
GO_LED  = 18
P1_LED  = 17
P2_LED  = 27
P1_BTN  = 5
P2_BTN  = 6

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in [GO_LED, P1_LED, P2_LED]:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    for pin in [P1_BTN, P2_BTN]:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def set_led(pin, state):
    if HARDWARE_MODE:
        GPIO.output(pin, GPIO.HIGH if state else GPIO.LOW)

def hardware_race():
    """Run one round using real GPIO buttons."""
    winner = None
    lock = threading.Lock()

    def check_button(player, btn_pin, led_pin):
        nonlocal winner
        while GPIO.input(btn_pin) == GPIO.HIGH:
            time.sleep(0.001)
        with lock:
            if winner is None:
                winner = player
                set_led(led_pin, True)

    p1_thread = threading.Thread(target=check_button, args=(1, P1_BTN, P1_LED), daemon=True)
    p2_thread = threading.Thread(target=check_button, args=(2, P2_BTN, P2_LED), daemon=True)
    p1_thread.start()
    p2_thread.start()

    # Wait for a winner
    start = time.perf_counter()
    while winner is None and time.perf_counter() - start < 5:
        time.sleep(0.001)

    return winner

def keyboard_race():
    """Keyboard simulation: who types their key first?"""
    import sys, select, tty, termios

    winner = None
    reaction_time = None

    print("  🎯 Press Z (P1) or M (P2) — GO!")
    start = time.perf_counter()

    # Simple approach: read input in a loop
    # (For proper non-blocking, we'd use select/tty — simplified here)
    try:
        inp = input("  First key (z or m): ").strip().lower()
        reaction_time = (time.perf_counter() - start) * 1000
        if 'z' in inp:
            winner = 1
        elif 'm' in inp:
            winner = 2
    except:
        pass

    return winner, reaction_time

def play_round_hardware(round_num, wins):
    """Play one round with hardware."""
    print(f"\n  Round {round_num} — get ready...")
    set_led(GO_LED, False)
    set_led(P1_LED, False)
    set_led(P2_LED, False)

    # Random wait
    wait = random.uniform(1.5, 4.0)
    time.sleep(wait)

    print("  ⚡ GO!")
    set_led(GO_LED, True)
    start = time.perf_counter()

    winner = hardware_race()
    reaction_ms = (time.perf_counter() - start) * 1000
    set_led(GO_LED, False)

    if winner:
        wins[winner] += 1
        print(f"  🏆 Player {winner} wins! ({reaction_ms:.0f}ms)")
    else:
        print("  ⏱ No one pressed in time!")

    time.sleep(2)
    return winner

def play_round_keyboard(round_num, wins):
    """Play one round with keyboard."""
    print(f"\n  Round {round_num} — get ready...")
    wait = random.uniform(2.0, 4.0)
    for i in range(3, 0, -1):
        print(f"  {i}...", end="\r", flush=True)
        time.sleep(1)
    print("  ⚡ GO! Press Z(P1) or M(P2)!")

    winner, reaction_ms = keyboard_race()

    if winner:
        wins[winner] += 1
        rms = f"{reaction_ms:.0f}ms" if reaction_ms else "?"
        print(f"  🏆 Player {winner} wins the round! ({rms})")
    else:
        print("  ❓ Invalid input — round skipped")

    return winner

def main():
    print("=" * 45)
    print("  ⚡ Two-Player Reaction Timer")
    print("=" * 45)

    if HARDWARE_MODE:
        setup()
        print("Hardware mode: 2 buttons + 3 LEDs")
    else:
        print("Simulation: Z=Player1, M=Player2")

    try:
        wins_to = int(input("\n  First to how many wins? (default 3): ").strip() or "3")
    except:
        wins_to = 3

    wins = {1: 0, 2: 0}
    round_num = 0

    print(f"\n  First to {wins_to} wins! Let's go!")
    print("  Player 1 — get your finger ready!")
    print("  Player 2 — get your finger ready!")

    try:
        while wins[1] < wins_to and wins[2] < wins_to:
            round_num += 1
            print(f"\n  Score: P1={wins[1]}  P2={wins[2]}")

            if HARDWARE_MODE:
                play_round_hardware(round_num, wins)
            else:
                play_round_keyboard(round_num, wins)

        print("\n" + "=" * 45)
        champion = 1 if wins[1] >= wins_to else 2
        print(f"  🏆 PLAYER {champion} IS THE CHAMPION! 🏆")
        print(f"  Final score: P1={wins[1]}  P2={wins[2]}")
        print("=" * 45)

    except KeyboardInterrupt:
        print("\n\n  Game stopped!")
    finally:
        if HARDWARE_MODE:
            for pin in [GO_LED, P1_LED, P2_LED]:
                GPIO.output(pin, GPIO.LOW)
            GPIO.cleanup()
        print("\n  Thanks for playing!")

if __name__ == "__main__":
    main()
