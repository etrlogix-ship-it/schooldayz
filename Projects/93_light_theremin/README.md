# 93 🎵 Light Theremin

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐⭐ Advanced  
**Time:** 40 minutes

## What You'll Make
A theremin is a musical instrument you play without touching it! This version uses a light sensor — wave your hand over it to change the pitch of the sound. More light = higher note!

## What You'll Learn
- Reading analogue sensor values (via ADC chip)
- Generating sound with Python
- Mapping sensor values to musical notes

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| Light Dependent Resistor (LDR/photoresistor) | 1 |
| MCP3008 ADC chip (optional for real analogue) | 1 |
| 10kΩ resistor | 1 |
| Buzzer (active or passive) | 1 |
| Breadboard | 1 |
| Jumper wires | 6 |

## How It Works
Light hits the LDR → resistance changes → Pi reads the value → maps it to a musical frequency → plays the note through the buzzer.

## How to Run
```bash
pip install pygame numpy
python3 light_theremin.py
```

Keyboard simulation mode available — use number keys to change pitch!

## Musical Notes Reference
```
C4=261Hz  D4=293Hz  E4=330Hz  F4=349Hz
G4=392Hz  A4=440Hz  B4=494Hz  C5=523Hz
```
