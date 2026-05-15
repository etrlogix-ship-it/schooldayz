# 91 🌈 RGB Colour Lamp

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 35 minutes

## What You'll Make
Build a colour-changing lamp using an RGB LED! Mix red, green, and blue light to create any colour you want. You can make it cycle through a rainbow, react to music, or set a custom mood colour.

## What You'll Learn
- Controlling RGB LEDs with PWM (Pulse Width Modulation)
- Mixing colours with light (additive colour mixing)
- Creating smooth colour transitions

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| RGB LED (common cathode) | 1 |
| 330Ω resistors | 3 |
| Breadboard | 1 |
| Jumper wires | 4 |

## Wiring
```
GPIO 17 (PWM) → 330Ω → Red pin   (RGB LED)
GPIO 18 (PWM) → 330Ω → Green pin (RGB LED)
GPIO 27 (PWM) → 330Ω → Blue pin  (RGB LED)
GND           →        GND pin   (RGB LED)
```

> **Common cathode** RGB LEDs have 4 legs. The longest leg is GND.

## How to Run
```bash
pip install RPi.GPIO
python3 rgb_lamp.py
```

## Colour Mixing Guide
| Red | Green | Blue | Result |
|-----|-------|------|--------|
| 255 | 0     | 0    | 🔴 Red |
| 0   | 255   | 0    | 🟢 Green |
| 0   | 0     | 255  | 🔵 Blue |
| 255 | 255   | 0    | 🟡 Yellow |
| 255 | 0     | 255  | 🟣 Magenta |
| 0   | 255   | 255  | 🩵 Cyan |
| 255 | 255   | 255  | ⚪ White |

## Fun Modes
- **Rainbow cycle** — smoothly cycles through all colours
- **Mood lamp** — slowly drifts between relaxing colours
- **Custom colour** — you pick exact R, G, B values
- **Party mode** — fast random colour flashes
