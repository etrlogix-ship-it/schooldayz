# 86 💡 LED Blinker

**Category:** Lights & Displays  
**Difficulty:** ⭐ Beginner  
**Time:** 20 minutes

## What You'll Make
Your very first physical computing project! Make an LED flash on and off using Python. It's the "Hello World" of electronics — once you can blink a light, you can control almost anything!

## What You'll Learn
- How to connect an LED to a Raspberry Pi
- Using GPIO pins to control hardware
- Writing loops that control real-world objects

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi (any model) | 1 |
| LED (any colour) | 1 |
| 330Ω resistor | 1 |
| Breadboard | 1 |
| Jumper wires | 2 |

## Wiring It Up
```
Raspberry Pi GPIO 18  →  Resistor (330Ω)  →  LED (+/long leg)
Raspberry Pi GND      →  LED (-/short leg)
```

> ⚠️ **Always use a resistor with an LED!** Without one, the LED will burn out instantly.

## How to Run

### Step 1 – Install the library
```bash
pip install RPi.GPIO
```

### Step 2 – Run it
```bash
cd code
python3 led_blinker.py
```

### Step 3 – Try the simulator (no hardware needed!)
The program has a **simulation mode** that works without any hardware. Just run it on any computer!

## What's Happening?
- The Pi sends a small electrical signal through GPIO pin 18
- This powers the LED through the resistor
- Python turns the pin HIGH (on) and LOW (off) in a loop
- The resistor limits current so the LED doesn't break

## Try Changing It!
- Make it blink faster or slower by changing `time.sleep(0.5)`
- Try a different pattern: 3 fast blinks, then a pause
- Use multiple LEDs on different pins for a chase effect

## Going Further
Once you can blink one LED, try:
- Project 87: Traffic Lights (3 LEDs!)
- Project 89: Simon Says (4 coloured LEDs)
