# 88 🎮 Button Reaction Game

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 30 minutes

## What You'll Make
A reaction speed game! An LED lights up at a random time and you press a button as fast as you can. Your reaction time is measured in milliseconds. Can you beat your high score?

## What You'll Learn
- Reading GPIO button inputs
- Measuring time with millisecond precision
- Storing and displaying high scores

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| LED (green) | 1 |
| Push button | 1 |
| 330Ω resistor (for LED) | 1 |
| Breadboard | 1 |
| Jumper wires | 4 |

## Wiring
```
GPIO 18  →  330Ω  →  LED (+)  →  GND
GPIO 24  →  Button one side   →  GND
         (use internal pull-up resistor in code)
```

## How to Run
```bash
pip install RPi.GPIO
python3 button_game.py
```

Simulation mode uses the keyboard — press ENTER when the light comes on!

## Game Rules
1. Watch the screen (or LED)
2. When it flashes GO — press the button as fast as you can!
3. Your reaction time is shown in milliseconds
4. Average human reaction time is about 250ms — can you beat it?

## Reaction Time Guide
| Time | Rating |
|------|--------|
| Under 150ms | 🏆 Lightning fast! |
| 150–200ms | ⭐⭐⭐ Excellent |
| 200–250ms | ⭐⭐ Good |
| 250–300ms | ⭐ Average |
| Over 300ms | 😴 Keep practising! |

## Try Changing It!
- Add a buzzer that beeps when the light turns on
- Make a two-player version on the same Pi
- Show a bar chart of your reaction times
