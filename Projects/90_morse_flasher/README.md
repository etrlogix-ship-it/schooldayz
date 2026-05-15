# 90 📡 Morse Code Flasher

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 25 minutes

## What You'll Make
Type any message and watch it get flashed out in real Morse code using an LED! This is how sailors and pilots used to send secret messages.

## What You'll Learn
- Morse code encoding
- Timing and pulsing LEDs
- Translating text into patterns

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| LED | 1 |
| 330Ω resistor | 1 |
| Breadboard | 1 |
| Jumper wires | 2 |

## Wiring
```
GPIO 18 → 330Ω → LED (+) → GND
```

## How to Run
```bash
pip install RPi.GPIO
python3 morse_flasher.py
```

## Morse Code Basics
- **Dot (·)** = short flash (0.2 seconds)
- **Dash (–)** = long flash (0.6 seconds)
- **Letter gap** = 0.4 seconds of darkness
- **Word gap** = 1.0 second of darkness

## Morse Code Chart
```
A ·–    B –···  C –·–·  D –··
E ·     F ··–·  G ––·   H ····
I ··    J ·–––  K –·–   L ·–··
M ––    N –·    O –––   P ·––·
Q ––·–  R ·–·   S ···   T –
U ··–   V ···–  W ·––   X –··–
Y –·––  Z ––··
```

## Try Changing It!
- Flash your name in Morse code
- Add a buzzer that beeps along with the flashes
- Write a decoder that takes Morse input and shows the letter
