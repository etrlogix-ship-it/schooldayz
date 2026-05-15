import time

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}
REVERSE = {v: k for k, v in MORSE.items()}

def to_morse(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text)

def from_morse(code):
    return ''.join(REVERSE.get(w, '?') for w in code.split(' '))

print("📡 Morse Code Translator")
print("========================")

while True:
    print("\n1) Text → Morse Code")
    print("2) Morse Code → Text")
    print("3) Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        text = input("Enter text: ")
        result = to_morse(text)
        print(f"\nMorse Code:\n{result}")
    elif choice == "2":
        code = input("Enter Morse code (use space between letters, / for space): ")
        result = from_morse(code)
        print(f"\nDecoded text: {result}")
    elif choice == "3":
        print("73 de Raspberry Pi! (That's ham radio for goodbye!)")
        break
    else:
        print("Invalid choice!")
