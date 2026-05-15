#!/usr/bin/env python3
"""
Button Reaction Game - Project 88
Test your reaction speed! Press the button when the LED lights up.
Works with hardware GPIO or keyboard simulation.
"""

import time
import random
import json
import os

try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
    print("✅ Raspberry Pi detected!")
except ImportError:
    HARDWARE_MODE = False

LED_PIN    = 18
BUTTON_PIN = 24
SCORES_FILE = "high_scores.json"

def setup():
    if not HARDWARE_MODE:
        return
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def led_on():
    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.HIGH)

def led_off():
    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.LOW)

def wait_for_button():
    """Wait for button press, returns True when pressed."""
    if HARDWARE_MODE:
        while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            time.sleep(0.001)
        return True
    else:
        input()  # keyboard simulation: press Enter
        return True

def rate_reaction(ms):
    if ms < 150:  return "🏆 LIGHTNING FAST!"
    if ms < 200:  return "⭐⭐⭐ Excellent!"
    if ms < 250:  return "⭐⭐ Good"
    if ms < 300:  return "⭐ Average"
    if ms < 400:  return "😐 A bit slow"
    return "😴 Keep practising!"

def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE) as f:
                return json.load(f)
        except:
            pass
    return {"best": None, "attempts": []}

def save_scores(scores):
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f)

def play_round(round_num):
    """Play one round of the reaction game. Returns reaction time in ms, or None if early press."""
    print(f"\n  Round {round_num}: Get ready...", end="", flush=True)

    # Random wait 1.5 – 4.5 seconds
    wait = random.uniform(1.5, 4.5)
    time.sleep(wait)

    # Light up!
    print("\n\n  ⚡⚡⚡  GO! PRESS NOW!  ⚡⚡⚡\n")
    led_on()
    start = time.perf_counter()

    # Wait for button
    wait_for_button()
    end = time.perf_counter()
    led_off()

    reaction_ms = (end - start) * 1000
    return reaction_ms

def show_bar(ms, best_ms):
    """Show a simple ASCII bar chart of the reaction time."""
    max_bar = 40
    scale   = 600  # 600ms = full bar
    filled  = min(max_bar, int(ms / scale * max_bar))
    bar     = "█" * filled + "░" * (max_bar - filled)
    print(f"  Your time:  [{bar}] {ms:.0f}ms")
    if best_ms:
        best_filled = min(max_bar, int(best_ms / scale * max_bar))
        best_bar    = "▓" * best_filled + "░" * (max_bar - best_filled)
        print(f"  Best ever:  [{best_bar}] {best_ms:.0f}ms")

def main():
    print("=" * 45)
    print("  🎮 Reaction Timer - Raspberry Pi Project")
    print("=" * 45)

    if HARDWARE_MODE:
        setup()
        print("Hardware mode: LED on GPIO 18, button on GPIO 24")
    else:
        print("Simulation mode: Press ENTER when you see GO!")

    scores = load_scores()
    if scores["best"]:
        print(f"\n  🏆 Current best: {scores['best']:.0f}ms")

    rounds = 5
    try:
        r = input("\nHow many rounds? (default 5): ").strip()
        if r.isdigit() and int(r) > 0:
            rounds = int(r)
    except:
        pass

    results = []
    print(f"\n▶ Starting {rounds} round game. Don't press early!")
    print("  Press ENTER to start first round..." if not HARDWARE_MODE else "  Press button to start first round...")
    wait_for_button()

    try:
        for i in range(1, rounds + 1):
            try:
                ms = play_round(i)
                if ms < 50:
                    print("  ⚡ Too fast — did you press early? Not counted.")
                    continue
                results.append(ms)
                rating = rate_reaction(ms)
                print(f"  ⏱  {ms:.0f} ms  —  {rating}")
                show_bar(ms, scores["best"])

                # Update best
                if scores["best"] is None or ms < scores["best"]:
                    scores["best"] = ms
                    print("  🎉 NEW PERSONAL BEST!")

                if i < rounds:
                    print("\n  Press button/Enter for next round...")
                    wait_for_button()

            except KeyboardInterrupt:
                print("\n  Round skipped.")
                break

        # Final summary
        if results:
            avg = sum(results) / len(results)
            best_this = min(results)
            print("\n" + "=" * 45)
            print("  📊 YOUR RESULTS")
            print("=" * 45)
            print(f"  Rounds played:   {len(results)}")
            print(f"  Best this game:  {best_this:.0f}ms")
            print(f"  Average:         {avg:.0f}ms")
            print(f"  All-time best:   {scores['best']:.0f}ms")
            print(f"\n  Overall rating: {rate_reaction(avg)}")

            scores["attempts"].extend(results)
            save_scores(scores)
            print(f"\n  Scores saved to {SCORES_FILE}")

    except KeyboardInterrupt:
        print("\n\n⏹ Game stopped.")

    finally:
        led_off()
        if HARDWARE_MODE:
            GPIO.cleanup()
        print("\n✅ Thanks for playing!")

if __name__ == "__main__":
    main()
