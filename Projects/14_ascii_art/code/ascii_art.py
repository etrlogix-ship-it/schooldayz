try:
    import pyfiglet
    USE_FIGLET = True
except ImportError:
    USE_FIGLET = False

def simple_banner(text):
    """Simple ASCII art without pyfiglet"""
    line = "=" * (len(text) + 4)
    print(line)
    print(f"| {text} |")
    print(line)

print("🎨 ASCII Art Generator!")
print("========================\n")

if USE_FIGLET:
    fonts = ["banner", "big", "block", "bubble", "digital", "slant", "standard"]
    print("Available fonts:", ", ".join(fonts))
else:
    print("Tip: Install pyfiglet for more fonts: pip3 install pyfiglet --break-system-packages")

while True:
    text = input("\nEnter text: ").strip()
    if not text:
        continue

    if USE_FIGLET:
        font = input(f"Choose font (press Enter for 'standard'): ").strip() or "standard"
        try:
            result = pyfiglet.figlet_format(text, font=font)
            print("\n" + result)
        except Exception:
            print("Font not found! Using standard.")
            print(pyfiglet.figlet_format(text))
    else:
        simple_banner(text.upper())

    if input("Make another? (yes/no): ").lower() != "yes":
        break
