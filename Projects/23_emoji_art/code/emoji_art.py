templates = {
    "sun": ["     🌟     ", "  🌟 ☀️  🌟  ", "     🌟     "],
    "house": ["    🔺🔺🔺    ", "  🟫🟫🟫🟫🟫  ", "  🟫🔵🟫🟫🟫  ", "  🟫🟫🚪🟫🟫  "],
    "rocket": ["   🚀   ", "  🔥🔥🔥 ", " 🔥🔥🔥🔥 "],
    "cat": ["  /\_/\  ", " ( o.o ) ", "  > ^ <  "]
}

print("Emoji Art Creator!")
print("==================")
print("Templates:", ", ".join(templates.keys()))

while True:
    choice = input("\nTemplate name (or custom): ").lower().strip()
    if choice in templates:
        for row in templates[choice]:
            print(row)
    elif choice == "custom":
        print("Enter emoji art line by line. Type done to finish:")
        lines = []
        while True:
            line = input()
            if line.lower() == "done":
                break
            lines.append(line)
        print("\nYour creation:")
        for l in lines:
            print(l)
    else:
        print("Template not found!")
    if input("\nMake another? (yes/no): ").lower() != "yes":
        break
