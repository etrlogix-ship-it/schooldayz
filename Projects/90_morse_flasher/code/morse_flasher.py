#!/usr/bin/env python3
"""
Morse Code Flasher - Project 90
Type a message and flash it in Morse code using an LED.
"""

import time

try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
    print("✅ Raspberry Pi detected!")
except ImportError:
    HARDWARE_MODE = False

LED_PIN = 18

MORSE_CODE = {
    'A': '.-',   'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',    'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',   'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',   'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-', 'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',  'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    ' ': ' '  # word gap
}

DOT  = 0.2   # dot duration (seconds)
DASH = DOT * 3
SYMBOL_GAP  = DOT
LETTER_GAP  = DOT * 3
WORD_GAP    = DOT * 7

def setup():
    if not HARDWARE_MODE:
        return
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

def flash(duration):
    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.HIGH)
    print("●", end="", flush=True)
    time.sleep(duration)
    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(SYMBOL_GAP)

def text_to_morse(text):
    morse = []
    for char in text.upper():
        if char == ' ':
            morse.append('/')
        elif char in MORSE_CODE:
            morse.append(MORSE_CODE[char])
        else:
            morse.append('?')
    return ' '.join(morse)

def flash_message(text):
    print(f"\n  Flashing: \"{text}\"")
    morse_str = text_to_morse(text)
    print(f"  Morse:    {morse_str}\n  Signal:   ", end="")

    for char in text.upper():
        if char == ' ':
            print("  /  ", end="", flush=True)
            time.sleep(WORD_GAP)
        elif char in MORSE_CODE:
            code = MORSE_CODE[char]
            for symbol in code:
                if symbol == '.':
                    flash(DOT)
                elif symbol == '-':
                    flash(DASH)
            time.sleep(LETTER_GAP - SYMBOL_GAP)
            print(" ", end="", flush=True)

    print("\n\n  ✅ Message sent!")

def show_morse_table():
    print("\n  MORSE CODE TABLE:")
    print("  " + "-" * 40)
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(0, len(letters), 4):
        row = letters[i:i+4]
        line = "  ".join(f"{l}: {MORSE_CODE[l]:<6}" for l in row)
        print(f"  {line}")

def main():
    print("=" * 45)
    print("  📡 Morse Code Flasher - Raspberry Pi")
    print("=" * 45)

    if HARDWARE_MODE:
        setup()
        print("LED connected on GPIO 18")
    else:
        print("Simulation mode (● = flash, space = gap)")

    while True:
        print("\n  Options:")
        print("  1. Flash a custom message")
        print("  2. Flash SOS")
        print("  3. Flash your name")
        print("  4. Show Morse code table")
        print("  5. Quit")
        choice = input("\n  Choice: ").strip()

        if choice == "1":
            msg = input("  Enter message: ").strip()
            if msg:
                flash_message(msg)

        elif choice == "2":
            flash_message("SOS")

        elif choice == "3":
            name = input("  Enter your name: ").strip()
            if name:
                flash_message(name)

        elif choice == "4":
            show_morse_table()

        elif choice == "5":
            break

        else:
            print("  Please enter 1-5")

    if HARDWARE_MODE:
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()
    print("\n  Goodbye! 73 de Pi (that's ham radio for 'best wishes from Pi')")

if __name__ == "__main__":
    main()
