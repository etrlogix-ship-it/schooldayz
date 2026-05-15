# 92 🎲 LED Dice

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 30 minutes

## What You'll Make
Roll a virtual dice using 7 LEDs arranged in the classic dice pattern! Press a button and the LEDs flash randomly before landing on a number 1–6, just like a real dice.

## What You'll Learn
- Controlling multiple LEDs as a display
- Dice dot patterns
- Random number generation with LEDs

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| LEDs (any colour) | 7 |
| 330Ω resistors | 7 |
| Push button | 1 |
| Breadboard | 1 |
| Jumper wires | 9 |

## Wiring (LED positions = dice dots)
```
Dice layout:   Top-left=GPIO5   Top-right=GPIO6
               Mid-left=GPIO13  Centre=GPIO19   Mid-right=GPIO26
               Bot-left=GPIO21  Bot-right=GPIO20

Button:        GPIO 17 → Button → GND
```

## How to Run
```bash
pip install RPi.GPIO
python3 led_dice.py
```

Simulation mode shows the dice pattern in ASCII art!

## The Dice Patterns
```
1: only centre
2: top-left, bottom-right
3: top-left, centre, bottom-right
4: all four corners
5: all four corners + centre
6: all six outer dots
```
