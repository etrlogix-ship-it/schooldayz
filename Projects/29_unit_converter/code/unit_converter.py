conversions = {
    "length": {
        "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
        "inch": 0.0254, "foot": 0.3048, "yard": 0.9144, "mile": 1609.34
    },
    "weight": {
        "mg": 0.000001, "g": 0.001, "kg": 1, "tonne": 1000,
        "ounce": 0.0283495, "pound": 0.453592, "stone": 6.35029
    },
    "speed": {
        "mph": 0.44704, "kph": 0.277778, "ms": 1, "knot": 0.514444
    }
}

print("Universal Unit Converter")
print("========================")

while True:
    print("\nCategories:", ", ".join(conversions.keys()))
    cat = input("Category (or quit): ").lower().strip()
    if cat == "quit": break
    if cat not in conversions:
        print("Unknown category!")
        continue
    units = conversions[cat]
    print("Units:", ", ".join(units.keys()))
    try:
        from_unit = input("From unit: ").lower()
        to_unit = input("To unit: ").lower()
        amount = float(input("Amount: "))
        if from_unit not in units or to_unit not in units:
            print("Unknown unit!")
            continue
        base = amount * units[from_unit]
        result = base / units[to_unit]
        print(f"{amount} {from_unit} = {result:.6g} {to_unit}")
    except ValueError:
        print("Please enter a valid number.")
