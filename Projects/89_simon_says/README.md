# 89 🎵 Simon Says

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐⭐ Advanced  
**Time:** 45 minutes

## What You'll Make
The classic memory game Simon Says! Four coloured LEDs light up in a sequence and you must repeat it by pressing the matching buttons. Each round the sequence gets one step longer. How far can you go?

## What You'll Learn
- Coordinating multiple GPIO inputs and outputs
- Memory/sequence games logic
- Debouncing button inputs

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| Red LED | 1 |
| Blue LED | 1 |
| Green LED | 1 |
| Yellow LED | 1 |
| Push buttons | 4 |
| 330Ω resistors (for LEDs) | 4 |
| Breadboard | 1 |
| Jumper wires | 12 |

## Wiring
```
GPIO 17 → 330Ω → Red LED    → GND    |  GPIO 5  → Button (Red)    → GND
GPIO 18 → 330Ω → Blue LED   → GND    |  GPIO 6  → Button (Blue)   → GND
GPIO 27 → 330Ω → Green LED  → GND    |  GPIO 13 → Button (Green)  → GND
GPIO 22 → 330Ω → Yellow LED → GND    |  GPIO 19 → Button (Yellow) → GND
```

## How to Run
```bash
pip install RPi.GPIO
python3 simon_says.py
```

Keyboard simulation: press R, B, G, Y keys instead of buttons!

## How to Play
1. Watch the sequence of lights (and listen to the tones)
2. Repeat the sequence by pressing the matching buttons
3. Each round adds one more step
4. One mistake and it's game over!

## Try Changing It!
- Make the sequence speed up as levels increase
- Add a buzzer for satisfying tones
- Save your high score between sessions
