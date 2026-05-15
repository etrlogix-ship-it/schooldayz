import random
import time

DICE_ART = {
    1: ["┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"],
    2: ["┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"],
    3: ["┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
    4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
    5: ["┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
    6: ["┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"],
}

print("🎲 Dice Roller!")
print("===============")

while True:
    try:
        num = int(input("\nHow many dice? (1-5): "))
        sides = int(input("How many sides? (default 6): ") or "6")
        if num < 1 or num > 5 or sides < 2:
            print("Please use 1-5 dice and at least 2 sides.")
            continue
    except ValueError:
        print("Enter numbers only!")
        continue

    print("\nRolling", "." * 5)
    time.sleep(0.5)

    rolls = [random.randint(1, sides) for _ in range(num)]
    
    if sides == 6 and all(r <= 6 for r in rolls):
        for row in range(5):
            print("  ".join(DICE_ART[r][row] for r in rolls))
    else:
        for i, r in enumerate(rolls):
            print(f"  Die {i+1}: {r}")

    print(f"\n  Total: {sum(rolls)}")

    if input("\nRoll again? (yes/no): ").lower() != "yes":
        break

print("Good luck with your game! 🎉")
