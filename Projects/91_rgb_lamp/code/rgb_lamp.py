#!/usr/bin/env python3
"""
RGB Colour Lamp - Project 91
Control an RGB LED to create any colour.
Uses PWM for smooth colour mixing.
"""

import time
import math
import random

try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
    print("✅ Raspberry Pi detected!")
except ImportError:
    HARDWARE_MODE = False

RED_PIN   = 17
GREEN_PIN = 18
BLUE_PIN  = 27
PWM_FREQ  = 100  # Hz

pwm_r = pwm_g = pwm_b = None

ANSI = {
    "red":     "\033[91m",
    "green":   "\033[92m",
    "yellow":  "\033[93m",
    "blue":    "\033[94m",
    "magenta": "\033[95m",
    "cyan":    "\033[96m",
    "white":   "\033[97m",
    "reset":   "\033[0m",
}

def setup():
    global pwm_r, pwm_g, pwm_b
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RED_PIN,   GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    GPIO.setup(BLUE_PIN,  GPIO.OUT)
    pwm_r = GPIO.PWM(RED_PIN,   PWM_FREQ)
    pwm_g = GPIO.PWM(GREEN_PIN, PWM_FREQ)
    pwm_b = GPIO.PWM(BLUE_PIN,  PWM_FREQ)
    pwm_r.start(0)
    pwm_g.start(0)
    pwm_b.start(0)

def set_colour(r, g, b):
    """Set RGB colour (0–255 each)."""
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    if HARDWARE_MODE:
        pwm_r.ChangeDutyCycle(r / 255 * 100)
        pwm_g.ChangeDutyCycle(g / 255 * 100)
        pwm_b.ChangeDutyCycle(b / 255 * 100)
    # Show colour in terminal using ANSI codes
    colour_block = f"R:{r:3d} G:{g:3d} B:{b:3d}"
    print(f"  🎨 {colour_block}  ████", end="\r", flush=True)

def hsv_to_rgb(h, s, v):
    """Convert HSV (0–360, 0–1, 0–1) to RGB (0–255)."""
    h = h % 360
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    if   h < 60:  r1,g1,b1 = c,x,0
    elif h < 120: r1,g1,b1 = x,c,0
    elif h < 180: r1,g1,b1 = 0,c,x
    elif h < 240: r1,g1,b1 = 0,x,c
    elif h < 300: r1,g1,b1 = x,0,c
    else:         r1,g1,b1 = c,0,x
    return int((r1+m)*255), int((g1+m)*255), int((b1+m)*255)

def rainbow_cycle(cycles=3, speed=0.01):
    """Smoothly cycle through all rainbow colours."""
    print(f"\n  🌈 Rainbow mode! ({cycles} cycles)")
    for _ in range(cycles * 360):
        hue = _ % 360
        r, g, b = hsv_to_rgb(hue, 1.0, 1.0)
        set_colour(r, g, b)
        time.sleep(speed)

def mood_lamp(duration=30):
    """Slowly drift between calming colours."""
    print(f"\n  🌙 Mood lamp ({duration}s)...")
    mood_colours = [
        (255,  60,  60),  # warm red
        (255, 120,   0),  # orange
        ( 60, 120, 255),  # calm blue
        ( 60, 200, 120),  # sea green
        (180,  60, 255),  # purple
        (255, 200,  60),  # golden yellow
    ]
    steps = 100
    start = time.time()
    ci = 0
    while time.time() - start < duration:
        r1,g1,b1 = mood_colours[ci % len(mood_colours)]
        r2,g2,b2 = mood_colours[(ci+1) % len(mood_colours)]
        for step in range(steps):
            if time.time() - start >= duration:
                break
            t = step / steps
            r = int(r1 + (r2-r1)*t)
            g = int(g1 + (g2-g1)*t)
            b = int(b1 + (b2-b1)*t)
            set_colour(r, g, b)
            time.sleep(0.05)
        ci += 1

def party_mode(duration=10):
    """Fast random colour flashes."""
    print(f"\n  🎉 Party mode! ({duration}s)")
    start = time.time()
    while time.time() - start < duration:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        set_colour(r, g, b)
        time.sleep(0.08)

def custom_colour():
    """Let user pick a colour."""
    named = {
        "red": (255,0,0), "green": (0,255,0), "blue": (0,0,255),
        "yellow": (255,255,0), "purple": (128,0,255), "cyan": (0,255,255),
        "white": (255,255,255), "orange": (255,128,0), "pink": (255,0,128),
        "off": (0,0,0)
    }
    print("\n  Named colours:", ", ".join(named.keys()))
    print("  Or enter R G B values (0-255 each)\n")
    inp = input("  Colour or R G B: ").strip().lower()
    if inp in named:
        r,g,b = named[inp]
    else:
        try:
            parts = inp.split()
            r,g,b = int(parts[0]), int(parts[1]), int(parts[2])
        except:
            print("  ❌ Couldn't parse that. Using red.")
            r,g,b = 255,0,0
    set_colour(r, g, b)
    print(f"\n  Set to R:{r} G:{g} B:{b}")
    input("  Press Enter to continue...")

def main():
    print("=" * 45)
    print("  🌈 RGB Colour Lamp - Raspberry Pi Project")
    print("=" * 45)

    if HARDWARE_MODE:
        setup()
    else:
        print("Simulation mode (colour shown in terminal)")

    try:
        while True:
            print("\n  🎨 Modes:")
            print("  1. Rainbow cycle")
            print("  2. Mood lamp (relaxing)")
            print("  3. Party mode (fast!)")
            print("  4. Custom colour")
            print("  5. Turn off")
            print("  6. Quit")
            choice = input("\n  Choice: ").strip()

            if choice == "1":
                try:
                    rainbow_cycle()
                except KeyboardInterrupt:
                    print("\n  Stopped.")

            elif choice == "2":
                try:
                    mood_lamp(60)
                except KeyboardInterrupt:
                    print("\n  Stopped.")

            elif choice == "3":
                try:
                    party_mode(15)
                except KeyboardInterrupt:
                    print("\n  Stopped.")

            elif choice == "4":
                custom_colour()

            elif choice == "5":
                set_colour(0, 0, 0)
                print("\n  Light off.")

            elif choice == "6":
                break

    except KeyboardInterrupt:
        print("\n\n  Stopped.")

    finally:
        set_colour(0, 0, 0)
        if HARDWARE_MODE:
            pwm_r.stop(); pwm_g.stop(); pwm_b.stop()
            GPIO.cleanup()
        print("  🌈 Lamp off. Goodbye!")

if __name__ == "__main__":
    main()
