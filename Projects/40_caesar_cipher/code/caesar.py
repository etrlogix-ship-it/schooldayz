def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def crack(text):
    print("\nAll possible decryptions:")
    for shift in range(1, 26):
        decrypted = decrypt(text, shift)
        print(f"  Shift {shift:2d}: {decrypted}")

print("Caesar Cipher")
print("=============")
print("The Caesar cipher shifts each letter by a fixed amount.")
print("Caesar himself used a shift of 3!")

while True:
    print("\n1) Encrypt  2) Decrypt  3) Crack (try all shifts)  4) Quit")
    choice = input("Choose: ")
    if choice == "1":
        msg = input("Message: ")
        try:
            shift = int(input("Shift (1-25): "))
            print(f"Encrypted: {encrypt(msg, shift)}")
        except ValueError:
            print("Invalid shift!")
    elif choice == "2":
        msg = input("Encrypted message: ")
        try:
            shift = int(input("Shift: "))
            print(f"Decrypted: {decrypt(msg, shift)}")
        except ValueError:
            print("Invalid shift!")
    elif choice == "3":
        msg = input("Message to crack: ")
        crack(msg)
    elif choice == "4":
        break
