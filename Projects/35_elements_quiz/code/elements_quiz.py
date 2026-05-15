import random

elements = [
    ("H", "Hydrogen", 1), ("He", "Helium", 2), ("Li", "Lithium", 3),
    ("C", "Carbon", 6), ("N", "Nitrogen", 7), ("O", "Oxygen", 8),
    ("Na", "Sodium", 11), ("Mg", "Magnesium", 12), ("Al", "Aluminium", 13),
    ("Si", "Silicon", 14), ("P", "Phosphorus", 15), ("S", "Sulfur", 16),
    ("Cl", "Chlorine", 17), ("K", "Potassium", 19), ("Ca", "Calcium", 20),
    ("Fe", "Iron", 26), ("Cu", "Copper", 29), ("Zn", "Zinc", 30),
    ("Au", "Gold", 79), ("Ag", "Silver", 47), ("Pb", "Lead", 82),
    ("U", "Uranium", 92)
]

score = 0
rounds = 10
print("Elements Quiz!")
print("==============")
for i in range(rounds):
    sym, name, num = random.choice(elements)
    mode = random.choice(["name", "symbol", "number"])
    if mode == "name":
        ans = input(f"Q{i+1}: What is the name of element with symbol '{sym}'? ").strip().title()
        if ans == name:
            print("Correct!"); score += 1
        else:
            print(f"Wrong! It is {name}.")
    elif mode == "symbol":
        ans = input(f"Q{i+1}: What is the chemical symbol for {name}? ").strip()
        if ans == sym:
            print("Correct!"); score += 1
        else:
            print(f"Wrong! It is {sym}.")
    else:
        ans = input(f"Q{i+1}: What is the atomic number of {name}? ").strip()
        if ans == str(num):
            print("Correct!"); score += 1
        else:
            print(f"Wrong! It is {num}.")
print(f"\nFinal score: {score}/{rounds}")
