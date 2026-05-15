#!/usr/bin/env python3
"""
Automatic Night Light - Project 95
LED turns on when it gets dark, off when it gets light.
Includes simulation mode and logging.
"""

import time
import random
import datetime
import os

try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
    print("✅ Raspberry Pi detected!")
except ImportError:
    HARDWARE_MODE = False

LED_PIN    = 18
SENSOR_PIN = 24   # Digital threshold from LDR voltage divider
LOG_FILE   = "light_log.txt"

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN,    GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(SENSOR_PIN, GPIO.IN)

def set_led(state):
    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.HIGH if state else GPIO.LOW)

def is_dark():
    """Return True if it's dark (sensor reads LOW)."""
    if HARDWARE_MODE:
        return GPIO.input(SENSOR_PIN) == GPIO.LOW
    return None  # simulation handles this elsewhere

def log_event(event, light_level=None):
    """Log a light change event."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp}  {event}"
    if light_level is not None:
        line += f"  (level={light_level}%)"
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

def simulate_day_night():
    """Simulate day/night cycle with user control."""
    print("\n  🌙 NIGHT LIGHT SIMULATOR")
    print("  " + "─" * 40)
    print("  Commands:")
    print("    'd' = simulate DAY   (light on → LED off)")
    print("    'n' = simulate NIGHT (dark → LED on)")
    print("    'a' = auto day/night cycle")
    print("    's' = show log")
    print("    'q' = quit\n")

    light_level = 80  # 0=pitch dark, 100=bright day
    led_on = False

    def update_display(level, led):
        bar_len = int(level / 5)
        bar = "☀" * bar_len + "·" * (20 - bar_len)
        led_icon = "💡 ON " if led else "○ OFF"
        print(f"  Light: [{bar}] {level:3d}%   LED: {led_icon}   ", end="\r")

    DARK_THRESHOLD = 30

    while True:
        update_display(light_level, led_on)
        cmd = input("\n  Command: ").strip().lower()

        if cmd == 'd':
            light_level = random.randint(60, 100)
            print(f"  ☀️  Daylight! Level: {light_level}%")
            if led_on:
                led_on = False
                set_led(False)
                log_event("LED OFF — it got light", light_level)
                print("  💡 LED turned OFF")

        elif cmd == 'n':
            light_level = random.randint(0, 25)
            print(f"  🌙 Night! Level: {light_level}%")
            if not led_on:
                led_on = True
                set_led(True)
                log_event("LED ON — it got dark", light_level)
                print("  💡 LED turned ON")

        elif cmd == 'a':
            print("\n  🔄 Auto cycle: Day → Dusk → Night → Dawn → Day")
            print("  (Press Ctrl+C to stop)\n")
            phases = [
                ("🌅 Dawn",   50, 3),
                ("☀️  Day",    90, 4),
                ("🌆 Dusk",   30, 3),
                ("🌙 Night",   5, 4),
            ]
            try:
                for cycle in range(3):
                    for phase_name, level, duration in phases:
                        light_level = level
                        dark = level < DARK_THRESHOLD
                        if dark and not led_on:
                            led_on = True
                            set_led(True)
                            log_event("LED ON — auto night", level)
                        elif not dark and led_on:
                            led_on = False
                            set_led(False)
                            log_event("LED OFF — auto day", level)
                        print(f"\n  {phase_name} (light={level}%) | LED={'ON' if led_on else 'OFF'}")
                        for _ in range(duration * 2):
                            update_display(light_level, led_on)
                            time.sleep(0.5)
            except KeyboardInterrupt:
                print("\n\n  Auto cycle stopped.")

        elif cmd == 's':
            if os.path.exists(LOG_FILE):
                print(f"\n  📋 Light log ({LOG_FILE}):")
                with open(LOG_FILE) as f:
                    lines = f.readlines()
                for line in lines[-10:]:  # last 10 events
                    print(f"  {line.rstrip()}")
            else:
                print("  No log yet — simulate some day/night cycles first!")

        elif cmd == 'q':
            break

        else:
            print("  Enter d, n, a, s, or q")

def hardware_mode_run():
    """Run the actual night light on real hardware."""
    setup()
    print("\n  🌙 Night light running... (Ctrl+C to stop)")
    print("  Cover the sensor to simulate night!\n")

    led_state = False
    last_state = None

    try:
        while True:
            dark = is_dark()
            if dark != last_state:
                if dark:
                    print(f"\n  🌙 It's dark! Turning LED on...")
                    set_led(True)
                    led_state = True
                    log_event("LED ON — sensor detected dark")
                else:
                    print(f"\n  ☀️  It's light! Turning LED off...")
                    set_led(False)
                    led_state = False
                    log_event("LED OFF — sensor detected light")
                last_state = dark

            status = "🌙 DARK → LED ON" if led_state else "☀️  LIGHT → LED off"
            print(f"  Status: {status}   ", end="\r")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n\n  Stopping night light...")
    finally:
        set_led(False)
        GPIO.cleanup()

def main():
    print("=" * 45)
    print("  🌙 Night Light - Raspberry Pi Project")
    print("=" * 45)

    if HARDWARE_MODE:
        print("Hardware mode — real LDR sensor")
        print("1. Run hardware mode")
        print("2. Run simulator")
        choice = input("Choice (1/2): ").strip()
        if choice == "1":
            hardware_mode_run()
            return

    simulate_day_night()
    set_led(False)
    if HARDWARE_MODE:
        GPIO.cleanup()
    print("\n  Night light off. Sleep well! 🌙")

if __name__ == "__main__":
    main()
