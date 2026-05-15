print("Binary & Number Systems Converter")
print("===================================")
print("Computers think in binary (base-2 — only 0s and 1s)!")
print("Let\'s explore different number systems.\n")
while True:
    print("\n1) Decimal to Binary/Hex/Octal")
    print("2) Binary to Decimal")
    print("3) Hex to Decimal")
    print("4) Quit")
    choice = input("Choose: ")
    if choice == "1":
        try:
            n = int(input("Enter a decimal number (0-1023): "))
            print(f"Decimal:  {n}")
            print(f"Binary:   {bin(n)} ({bin(n)[2:]})")
            print(f"Hexadecimal: {hex(n).upper()} ({hex(n)[2:].upper()})")
            print(f"Octal:    {oct(n)} ({oct(n)[2:]})")
        except ValueError:
            print("Invalid number!")
    elif choice == "2":
        b = input("Enter a binary number (e.g. 1010): ").strip()
        try:
            print(f"Binary {b} = Decimal {int(b, 2)}")
        except ValueError:
            print("Invalid binary number!")
    elif choice == "3":
        h = input("Enter hex (e.g. FF): ").strip()
        try:
            print(f"Hex {h} = Decimal {int(h, 16)}")
        except ValueError:
            print("Invalid hex number!")
    elif choice == "4":
        break
