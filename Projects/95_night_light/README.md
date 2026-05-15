# 95 🌙 Automatic Night Light

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 30 minutes

## What You'll Make
Build a night light that turns on automatically when it gets dark and off when it's light! Just like the lights that come on in the street at night. This is a real-world automation project!

## What You'll Learn
- Reading analogue sensors with GPIO
- Threshold-based automation
- Making a device that runs without human input

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| LED (warm white or yellow) | 1 |
| Light Dependent Resistor (LDR) | 1 |
| 10kΩ resistor (voltage divider) | 1 |
| 330Ω resistor (for LED) | 1 |
| MCP3008 ADC (for true analogue) | 1 |
| Breadboard | 1 |
| Jumper wires | 6 |

## Wiring
```
GPIO 18 → 330Ω → LED     → GND
3.3V    → 10kΩ → LDR     → GPIO 24 (threshold detection)
                  LDR bottom → GND
```

## How to Run
```bash
pip install RPi.GPIO
python3 night_light.py
```

## How It Works
1. The LDR (light sensor) changes resistance based on light levels
2. In a voltage divider circuit, this creates a threshold voltage
3. When it gets dark (voltage drops), GPIO pin reads LOW
4. The LED switches ON automatically!
5. When light returns, the LED switches OFF

## Try Changing It!
- Adjust the sensitivity threshold
- Add a dimmer effect that slowly fades the light on/off
- Log the light/dark times to a file
- Add a buzzer for a sunrise alarm
