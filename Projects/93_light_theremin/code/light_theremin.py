#!/usr/bin/env python3
"""
Light Theremin - Project 93
Wave your hand over a light sensor to play musical notes.
Keyboard simulation included for non-hardware use.
"""

import time
import math
import threading

# Try hardware imports
try:
    import RPi.GPIO as GPIO
    HARDWARE_MODE = True
except ImportError:
    HARDWARE_MODE = False

try:
    import pygame
    import numpy as np
    AUDIO_MODE = True
    pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
except ImportError:
    AUDIO_MODE = False

NOTES = {
    "C4": 261.63, "D4": 293.66, "E4": 329.63, "F4": 349.23,
    "G4": 392.00, "A4": 440.00, "B4": 493.88, "C5": 523.25,
    "D5": 587.33, "E5": 659.25, "F5": 698.46, "G5": 783.99,
}
NOTE_NAMES = list(NOTES.keys())

SAMPLE_RATE = 44100

def generate_tone(freq, duration=0.15, volume=0.3):
    """Generate a sine wave tone as pygame Sound."""
    if not AUDIO_MODE:
        return None
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = np.sin(2 * np.pi * freq * t) * volume
    # Fade in/out to avoid clicks
    fade = 100
    wave[:fade]  *= np.linspace(0, 1, fade)
    wave[-fade:] *= np.linspace(1, 0, fade)
    audio = (wave * 32767).astype(np.int16)
    return pygame.sndarray.make_sound(audio)

def play_note(freq):
    if AUDIO_MODE:
        sound = generate_tone(freq)
        if sound:
            sound.play()

def simulate_theremin():
    """Keyboard simulation of the theremin."""
    print("\n  🎵 KEYBOARD THEREMIN MODE")
    print("  Keys 1-9 = different notes, 0 = off")
    print("  Press Ctrl+C to stop\n")

    key_map = {
        '1': 'C4', '2': 'D4', '3': 'E4', '4': 'F4',
        '5': 'G4', '6': 'A4', '7': 'B4', '8': 'C5',
        '9': 'D5', '0': None
    }

    print("  Note scale:")
    for k, n in key_map.items():
        if n:
            freq = NOTES[n]
            print(f"    [{k}] {n:4s} = {freq:.0f}Hz")

    print("\n  Enter notes one at a time (e.g. '1 2 3 4 5'):")
    print("  Or type 'demo' to hear a demo melody\n")

    while True:
        try:
            inp = input("  Notes: ").strip().lower()
            if inp == 'demo':
                melody = ['1','2','3','4','5','4','3','2','1']
                print("  🎵 Playing demo...")
                for k in melody:
                    note = key_map.get(k)
                    if note:
                        freq = NOTES[note]
                        print(f"  ♪ {note} ({freq:.0f}Hz)", end="\r")
                        play_note(freq)
                    time.sleep(0.3)
                print()
            else:
                for char in inp.split():
                    note = key_map.get(char)
                    if note:
                        freq = NOTES[note]
                        bar_len = int((freq - 250) / 20)
                        bar = "▓" * min(bar_len, 30)
                        print(f"  ♪ {note:4s} {freq:6.1f}Hz [{bar}]")
                        play_note(freq)
                        time.sleep(0.25)
                    elif char == '0':
                        print("  (silence)")
        except KeyboardInterrupt:
            print("\n\n  Theremin off!")
            break
        except EOFError:
            break

def main():
    print("=" * 45)
    print("  🎵 Light Theremin - Raspberry Pi Project")
    print("=" * 45)

    if not AUDIO_MODE:
        print("⚠️  pygame/numpy not found — showing frequency only (no sound)")
        print("   Install with: pip install pygame numpy\n")
    else:
        print("🔊 Audio mode active")

    if HARDWARE_MODE:
        print("🔌 Raspberry Pi hardware mode")
        print("   Connect LDR + MCP3008 to use light sensor")
        print("   (Falling back to keyboard simulation)\n")
    else:
        print("💻 Simulation mode\n")

    simulate_theremin()

if __name__ == "__main__":
    main()
