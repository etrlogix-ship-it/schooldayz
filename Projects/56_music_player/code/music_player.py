try:
    import pygame
    import numpy as np
    pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)
    HAS_PYGAME = True
except ImportError:
    HAS_PYGAME = False

import math, time

NOTES = {
    "a": ("C4", 261.63),
    "s": ("D4", 293.66),
    "d": ("E4", 329.63),
    "f": ("F4", 349.23),
    "g": ("G4", 392.00),
    "h": ("A4", 440.00),
    "j": ("B4", 493.88),
    "k": ("C5", 523.25),
    "w": ("C#4", 277.18),
    "e": ("D#4", 311.13),
    "t": ("F#4", 369.99),
    "y": ("G#4", 415.30),
    "u": ("A#4", 466.16),
}

def play_note(freq, duration=0.3):
    if not HAS_PYGAME:
        print(f"NOTE: {freq:.1f}Hz (install pygame for sound)")
        return
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    envelope = np.exp(-3 * t / duration)
    wave = (wave * envelope * 32767).astype(np.int16)
    sound = pygame.sndarray.make_sound(wave)
    sound.play()
    time.sleep(duration)

print("Music Note Player!")
print("==================")
print("Keys to notes:")
for key, (note, freq) in NOTES.items():
    print(f"  [{key}] = {note} ({freq:.1f}Hz)")
print("\nType keys to play notes (q to quit):")

import sys
if sys.platform != "win32":
    import tty, termios
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == "q": break
            if ch in NOTES:
                note, freq = NOTES[ch]
                print(f"\r{note}  ", end="", flush=True)
                play_note(freq, 0.4)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
else:
    while True:
        ch = input("Key: ").lower()[:1]
        if ch == "q": break
        if ch in NOTES:
            note, freq = NOTES[ch]
            print(f"{note}")
            play_note(freq, 0.4)

print("\nThanks for playing!")
