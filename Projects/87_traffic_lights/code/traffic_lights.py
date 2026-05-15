#!/usr/bin/env python3
"""
Traffic Lights - Project 87
Simulate a traffic light with red, yellow, and green LEDs.
Includes pedestrian crossing mode and simulation for non-Pi computers.
"""

import time
import threading

try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
    print("✅ Raspberry Pi detected!")
except ImportError:
    HARDWARE_MODE = False

# GPIO pin assignments
RED_PIN    = 17
YELLOW_PIN = 27
GREEN_PIN  = 22
BUTTON_PIN = 4   # pedestrian crossing button (optional)

# Timing (seconds)
RED_TIME    = 3.0
YELLOW_TIME = 1.0
GREEN_TIME  = 3.0

# State
pedestrian_waiting = False

LIGHT_DISPLAY = {
    "red":    "🔴 RED    ████░░░░",
    "yellow": "🟡 YELLOW ░░████░░",
    "green":  "🟢 GREEN  ░░░░████",
    "off":    "⬛ OFF    ░░░░░░░░",
}

def setup():
    if not HARDWARE_MODE:
        return
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RED_PIN,    GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(YELLOW_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(GREEN_PIN,  GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING,
                          callback=pedestrian_button_pressed, bouncetime=300)

def pedestrian_button_pressed(channel=None):
    global pedestrian_waiting
    pedestrian_waiting = True
    print("\n  🚶 Pedestrian crossing requested!")

def set_lights(red=False, yellow=False, green=False):
    """Set the state of all three lights."""
    if HARDWARE_MODE:
        GPIO.output(RED_PIN,    GPIO.HIGH if red    else GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.HIGH if yellow else GPIO.LOW)
        GPIO.output(GREEN_PIN,  GPIO.HIGH if green  else GPIO.LOW)

def display_light(state, remaining=None):
    """Show current light state in terminal."""
    icon = LIGHT_DISPLAY.get(state, "")
    if remaining is not None:
        print(f"  {icon}  ({remaining:.0f}s remaining)  ", end="\r")
    else:
        print(f"  {icon}                    ")

def show_phase(state, duration, can_interrupt=False):
    """Show a traffic light phase with countdown."""
    global pedestrian_waiting

    colors = {"red": (True,False,False), "yellow": (False,True,False), "green": (False,False,True)}
    r, y, g = colors.get(state, (False,False,False))
    set_lights(r, y, g)

    start = time.time()
    while time.time() - start < duration:
        remaining = duration - (time.time() - start)
        display_light(state, remaining)
        time.sleep(0.1)

        if can_interrupt and pedestrian_waiting and state == "green":
            if remaining > 1.5:
                print(f"\n  ⏩ Cutting green short for pedestrian...")
                break

    set_lights(False, False, False)
    print()

def run_normal_cycle(cycles):
    """Run the standard traffic light sequence."""
    for cycle in range(1, cycles + 1):
        print(f"\n--- Cycle {cycle}/{cycles} ---")

        # Red
        print("  🛑 STOP")
        show_phase("red", RED_TIME)

        # Red + Yellow (get ready)
        print("  🟡 GET READY...")
        show_phase("yellow", YELLOW_TIME)

        # Green — can be cut short for pedestrians
        print("  ✅ GO!")
        show_phase("green", GREEN_TIME, can_interrupt=True)

        # Handle pedestrian crossing
        if pedestrian_waiting:
            handle_pedestrian_crossing()

        # Yellow (caution)
        print("  ⚠️  CAUTION")
        show_phase("yellow", YELLOW_TIME)

def handle_pedestrian_crossing():
    global pedestrian_waiting
    pedestrian_waiting = False
    print("\n  🚶 PEDESTRIAN CROSSING!")
    print("  " + "=" * 30)
    set_lights(red=True)
    display_light("red")
    for i in range(5, 0, -1):
        print(f"  🚶 Walk signal: {i}s  ", end="\r")
        time.sleep(1)
    print("\n  🛑 Don't walk!")
    time.sleep(1)
    set_lights(False, False, False)

def keyboard_simulation():
    """Let user simulate the pedestrian button with keyboard."""
    print("\n  💡 TIP: Type 'p' and press Enter to simulate pedestrian button!")
    print("         (This simulates pressing the crossing button)\n")

    def watch_input():
        while True:
            try:
                user = input()
                if user.lower() == 'p':
                    pedestrian_button_pressed()
                elif user.lower() == 'q':
                    break
            except EOFError:
                break

    t = threading.Thread(target=watch_input, daemon=True)
    t.start()

def main():
    global pedestrian_waiting

    print("=" * 45)
    print("  🚦 Traffic Lights - Raspberry Pi Project")
    print("=" * 45)

    if HARDWARE_MODE:
        setup()
        print("Hardware mode: GPIO pins active")
    else:
        print("Simulation mode: No hardware needed")

    print("\nChoose mode:")
    print("  1. Normal traffic light (5 cycles)")
    print("  2. Demo mode (fast, 3 cycles)")
    print("  3. Pedestrian crossing demo")
    choice = input("\nEnter choice (1-3): ").strip()

    try:
        if choice == "2":
            # Fast demo
            global RED_TIME, YELLOW_TIME, GREEN_TIME
            RED_TIME = 1.5; YELLOW_TIME = 0.5; GREEN_TIME = 1.5
            print("\n▶ Fast demo mode (3 cycles)...")
            run_normal_cycle(3)

        elif choice == "3":
            print("\n▶ Pedestrian crossing demo...")
            print("  The light will go green, then a pedestrian will press the button.\n")
            # Simulate a pedestrian pressing after 1s
            def press_button():
                time.sleep(1.5)
                pedestrian_button_pressed()
            threading.Thread(target=press_button, daemon=True).start()
            run_normal_cycle(2)

        else:
            print("\n▶ Normal traffic light (5 cycles)")
            if not HARDWARE_MODE:
                keyboard_simulation()
            run_normal_cycle(5)

    except KeyboardInterrupt:
        print("\n\n⏹ Stopped by user.")

    finally:
        set_lights(False, False, False)
        if HARDWARE_MODE:
            GPIO.cleanup()
        print("\n✅ All lights off. Goodbye!")

if __name__ == "__main__":
    main()
