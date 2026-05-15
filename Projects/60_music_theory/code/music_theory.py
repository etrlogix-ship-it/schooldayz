import random

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
intervals = {
    1: "Minor 2nd", 2: "Major 2nd", 3: "Minor 3rd", 4: "Major 3rd",
    5: "Perfect 4th", 6: "Tritone", 7: "Perfect 5th", 8: "Minor 6th",
    9: "Major 6th", 10: "Minor 7th", 11: "Major 7th", 12: "Octave"
}

scales = {
    "Major": [0, 2, 4, 5, 7, 9, 11],
    "Minor": [0, 2, 3, 5, 7, 8, 10],
    "Pentatonic Major": [0, 2, 4, 7, 9],
    "Blues": [0, 3, 5, 6, 7, 10],
}

def build_scale(root, scale_type):
    root_idx = notes.index(root)
    return [notes[(root_idx + step) % 12] for step in scales[scale_type]]

print("Music Theory Trainer")
print("====================")
while True:
    print("\n1) Interval quiz  2) Scale builder  3) Chord notes quiz  4) Quit")
    choice = input("Choose: ")
    if choice == "1":
        score = 0
        for _ in range(5):
            semitones = random.randint(1, 12)
            correct = intervals[semitones]
            options = random.sample([v for k,v in intervals.items() if k != semitones], 3) + [correct]
            random.shuffle(options)
            print(f"\nWhat is an interval of {semitones} semitones?")
            for i, o in enumerate(options): print(f"  {i+1}. {o}")
            try:
                ans = int(input("Your answer: ")) - 1
                if options[ans] == correct:
                    print("Correct!"); score += 1
                else:
                    print(f"Wrong! It was: {correct}")
            except (ValueError, IndexError): pass
        print(f"Score: {score}/5")
    elif choice == "2":
        root = input("Root note (C/D/E/F/G/A/B + optional #): ").strip().upper()
        if root not in notes:
            print("Invalid note!")
            continue
        print("Scale types:", ", ".join(scales.keys()))
        scale_type = input("Scale type: ").strip().title()
        if scale_type in scales:
            print(f"{root} {scale_type} scale: {' '.join(build_scale(root, scale_type))}")
        else:
            print("Unknown scale!")
    elif choice == "4":
        break
