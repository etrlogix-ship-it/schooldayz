# 94 ⚡ Two-Player Reaction Timer

**Category:** Lights & Displays  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 30 minutes

## What You'll Make
A two-player reaction speed competition! Both players get a button. When the light turns green, whoever presses their button first wins! Great for settling arguments about who has faster reflexes.

## What You'll Learn
- Multi-input GPIO reading
- First-to-fire detection
- Best-of-N game logic

## Parts You'll Need
| Part | Quantity |
|------|----------|
| Raspberry Pi | 1 |
| Green LED (go signal) | 1 |
| Red LED (player 1 wins) | 1 |
| Blue LED (player 2 wins) | 1 |
| Push buttons | 2 |
| 330Ω resistors | 3 |
| Breadboard | 1 |
| Jumper wires | 8 |

## Wiring
```
GPIO 18 → 330Ω → Green LED  → GND    (go signal)
GPIO 17 → 330Ω → Red LED    → GND    (P1 wins)
GPIO 27 → 330Ω → Blue LED   → GND    (P2 wins)
GPIO 5  → Button (Player 1) → GND
GPIO 6  → Button (Player 2) → GND
```

## How to Play
1. Both players put a finger on their button — but DON'T press yet!
2. The program counts down
3. When the GREEN light flashes — press as fast as you can!
4. First to press wins the round
5. First to win 3 rounds wins the game!

## Simulation Mode
Two keyboard keys simulate the buttons:
- **Z key** = Player 1
- **M key** = Player 2
