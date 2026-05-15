import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def password_strength(pwd):
    score = 0
    if len(pwd) >= 8: score += 1
    if len(pwd) >= 12: score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in "!@#$%^&*" for c in pwd): score += 1
    levels = {5: "🟢 Very Strong", 4: "🟡 Strong", 3: "🟠 Medium", 2: "🔴 Weak", 1: "⛔ Very Weak"}
    return levels.get(score, "⛔ Very Weak")

print("🔐 Password Generator")
print("=====================")

while True:
    try:
        length = int(input("\nPassword length (8-50, default 16): ") or "16")
        length = max(8, min(50, length))
    except ValueError:
        length = 16

    use_upper = input("Include uppercase? (yes/no, default yes): ").lower() != "no"
    use_digits = input("Include numbers? (yes/no, default yes): ").lower() != "no"
    use_symbols = input("Include symbols? (yes/no, default yes): ").lower() != "no"

    print("\nGenerated passwords:")
    for i in range(5):
        pwd = generate_password(length, use_upper, use_digits, use_symbols)
        strength = password_strength(pwd)
        print(f"  {i+1}. {pwd}  ({strength})")

    if input("\nGenerate more? (yes/no): ").lower() != "yes":
        break

print("\nRemember: Never share your passwords! Stay safe online! 🛡️")
