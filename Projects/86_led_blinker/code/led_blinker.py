#!/usr/bin/env python3
"""
LED Blinker - Project 86
Make an LED blink using Raspberry Pi GPIO pins.
Includes simulation mode for computers without hardware.
"""

import time
import sys

# Try to import GPIO library (only works on Raspberry Pi)
try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
    print("✅ Raspberry Pi detected - using real GPIO pins!")
except ImportError:
    HARDWARE_MODE = False
    print("💻 No GPIO hardware found - running in simulation mode")
    print("   (Run this on a Raspberry Pi with an LED connected to use real hardware)\n")

# --- Configuration ---
LED_PIN = 18          # GPIO pin number (BCM numbering)
BLINK_ON  = 0.5       # seconds LED stays ON
BLINK_OFF = 0.5       # seconds LED stays OFF
BLINK_COUNT = 20      # how many times to blink (0 = forever)

def setup_gpio():
    """Set up the GPIO pin for output."""
    GPIO.setmode(GPIO.BCM)          # use BCM pin numbering
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)  # start with LED off

def led_on():
    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        print("💡 LED ON  ████████", end="\r")

def led_off():
    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.LOW)
    else:
        print("   LED OFF ░░░░░░░░", end="\r")

def cleanup():
    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()

def blink_pattern(pattern):
    """
    Blink an LED using a pattern of (on_time, off_time) tuples.
    Example pattern for SOS: [(0.2,0.2),(0.2,0.2),(0.2,0.4),
                               (0.5,0.2),(0.5,0.2),(0.5,0.4),
                               (0.2,0.2),(0.2,0.2),(0.2,1.0)]
    """
    for on_time, off_time in pattern:
        led_on()
        time.sleep(on_time)
        led_off()
        time.sleep(off_time)

def choose_mode():
    print("\n🌟 LED Blinker - Choose a mode:\n")
    print("  1. Simple blink (on/off)")
    print("  2. Fast blink")
    print("  3. Heartbeat pulse")
    print("  4. SOS morse code")
    print("  5. Custom speed")
    print("  6. Blink forever (Ctrl+C to stop)")
    print()
    return input("Enter choice (1-6): ").strip()

def main():
    print("=" * 40)
    print("  💡 LED Blinker - Raspberry Pi Project")
    print("=" * 40)

    if HARDWARE_MODE:
        setup_gpio()

    choice = choose_mode()

    try:
        if choice == "1":
            print("\n▶ Simple blink (20 times)...")
            for i in range(20):
                led_on()
                time.sleep(0.5)
                led_off()
                time.sleep(0.5)
                print(f"  Blink {i+1}/20")

        elif choice == "2":
            print("\n⚡ Fast blink (30 times)...")
            for i in range(30):
                led_on()
                time.sleep(0.1)
                led_off()
                time.sleep(0.1)

        elif choice == "3":
            print("\n💓 Heartbeat pulse (15 beats)...")
            for _ in range(15):
                # Double-pulse like a heartbeat
                led_on();  time.sleep(0.1)
                led_off(); time.sleep(0.1)
                led_on();  time.sleep(0.1)
                led_off(); time.sleep(0.6)

        elif choice == "4":
            print("\n📡 SOS morse code (3 times)...")
            dot  = 0.2
            dash = 0.6
            gap  = 0.2
            letter_gap = 0.4
            word_gap   = 1.0
            sos_pattern = (
                # S = ...
                [(dot, gap), (dot, gap), (dot, letter_gap)] +
                # O = ---
                [(dash, gap), (dash, gap), (dash, letter_gap)] +
                # S = ...
                [(dot, gap), (dot, gap), (dot, word_gap)]
            )
            for _ in range(3):
                blink_pattern(sos_pattern)
            print("\n  SOS sent! (dit-dit-dit  dah-dah-dah  dit-dit-dit)")

        elif choice == "5":
            speed = input("\nEnter blink speed in seconds (e.g. 0.3): ").strip()
            try:
                delay = float(speed)
                count = int(input("How many blinks? ").strip())
                print(f"\n▶ Blinking {count} times at {delay}s interval...")
                for i in range(count):
                    led_on()
                    time.sleep(delay)
                    led_off()
                    time.sleep(delay)
            except ValueError:
                print("❌ Invalid input. Using default 0.5s, 10 blinks.")
                for _ in range(10):
                    led_on();  time.sleep(0.5)
                    led_off(); time.sleep(0.5)

        elif choice == "6":
            print("\n🔄 Blinking forever... press Ctrl+C to stop")
            count = 0
            while True:
                led_on()
                time.sleep(0.5)
                led_off()
                time.sleep(0.5)
                count += 1
                if not HARDWARE_MODE:
                    print(f"  Blink count: {count}     ", end="\r")

        else:
            print("Running simple blink as default...")
            for _ in range(10):
                led_on();  time.sleep(0.5)
                led_off(); time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n\n⏹ Stopped by user.")

    finally:
        led_off()
        cleanup()
        print("\n✅ Done! LED turned off safely.")
        if HARDWARE_MODE:
            print("   GPIO pins cleaned up.")

if __name__ == "__main__":
    main()
