import math, time

def draw_wave(freq, amplitude, width=60, height=15):
    """Draw a sine wave in the terminal"""
    print(f"Frequency: {freq}Hz  Amplitude: {amplitude}")
    print("+" + "-" * width + "+")
    for row in range(height):
        y = ((height-1)/2 - row) / ((height-1)/2)
        line = ""
        for col in range(width):
            x = col / width * 2 * math.pi * freq / 2
            wave_y = amplitude * math.sin(x)
            char = "●" if abs(wave_y - y) < 0.15 else " "
            line += char
        print("|" + line + "|")
    print("+" + "-" * width + "+")

print("Wave Explorer")
print("=============")
print("Explore how different frequencies look as waves!
")

while True:
    print("\n1) Draw a wave  2) Compare waves  3) Frequency facts  4) Quit")
    choice = input("Choose: ")
    if choice == "1":
        try:
            freq = float(input("Frequency (1-5): ") or "2")
            freq = max(1, min(5, freq))
            draw_wave(freq, 0.8)
        except ValueError: pass
    elif choice == "2":
        for f in [1, 2, 4]:
            draw_wave(f, 0.8)
            time.sleep(0.5)
    elif choice == "3":
        print("\nFrequency facts:")
        print("  • 20Hz - lowest humans can hear (bass rumble)")
        print("  • 440Hz - concert A (middle A on piano)")
        print("  • 4000Hz - most sensitive range of human hearing")
        print("  • 20,000Hz - highest humans can hear")
        print("  • Dogs can hear up to 65,000Hz!")
    elif choice == "4": break
