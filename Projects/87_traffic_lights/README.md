# 87 🚦 Traffic Lights

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 30 minutes

## What You'll Make
Build a working traffic light system with red, yellow, and green LEDs! You'll program the correct traffic light sequence and even add a pedestrian crossing button.

## What You'll Learn
- Controlling multiple GPIO outputs at once
- Timed sequences and state machines
- Reading button inputs (bonus feature)

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| Red LED | 1 |
| Yellow LED | 1 |
| Green LED | 1 |
| 330Ω resistors | 3 |
| Push button (optional) | 1 |
| Breadboard | 1 |
| Jumper wires | 6+ |

## Wiring It Up
```
GPIO 17  →  330Ω  →  Red LED    →  GND
GPIO 27  →  330Ω  →  Yellow LED →  GND
GPIO 22  →  330Ω  →  Green LED  →  GND
GPIO 4   →  Button  →  GND  (optional pedestrian button)
```

## How to Run
```bash
pip install RPi.GPIO
python3 traffic_lights.py
```

Simulation mode works on any computer — just run it without hardware!

## The Traffic Light Sequence
```
🔴 Red    (stop)   → 3 seconds
🟡 Yellow (ready)  → 1 second
🟢 Green  (go)     → 3 seconds
🟡 Yellow (caution)→ 1 second
🔴 Red    (stop)   → repeat
```

## Try Changing It!
- Adjust the timing of each phase
- Add a buzzer that beeps during pedestrian crossing
- Create a second set of lights for crossing traffic
