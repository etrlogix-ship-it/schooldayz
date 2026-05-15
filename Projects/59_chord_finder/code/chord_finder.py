chords = {
    "C":  {"notes": ["C","E","G"], "frets": "x32010", "desc": "C Major — sunny, happy sound"},
    "D":  {"notes": ["D","F#","A"], "frets": "xx0232", "desc": "D Major — bright, bold"},
    "E":  {"notes": ["E","G#","B"], "frets": "022100", "desc": "E Major — full, rich sound"},
    "G":  {"notes": ["G","B","D"], "frets": "320003", "desc": "G Major — resonant, open"},
    "A":  {"notes": ["A","C#","E"], "frets": "x02220", "desc": "A Major — bright, clear"},
    "Am": {"notes": ["A","C","E"], "frets": "x02210", "desc": "A Minor — sad, reflective"},
    "Em": {"notes": ["E","G","B"], "frets": "022000", "desc": "E Minor — deep, moody"},
    "F":  {"notes": ["F","A","C"], "frets": "133211", "desc": "F Major — warm, triumphant"},
    "Dm": {"notes": ["D","F","A"], "frets": "xx0231", "desc": "D Minor — melancholy"},
    "Bm": {"notes": ["B","D","F#"], "frets": "x24432", "desc": "B Minor — dark, intense"},
}

print("Guitar Chord Finder")
print("===================")
print("Available chords:", ", ".join(chords.keys()))

while True:
    name = input("\nChord name (or quit): ").strip()
    if name.lower() == "quit": break
    if name in chords:
        c = chords[name]
        print(f"\n{name} chord")
        print(f"  Notes: {', '.join(c['notes'])}")
        print(f"  Frets: {c['frets']}")
        print(f"  Description: {c['desc']}")
        print("\n  String: E A D G B e")
        print(f"  Frets:  {' '.join(c['frets'])}")
    else:
        similar = [k for k in chords if name.upper() in k.upper()]
        if similar:
            print(f"Not found. Did you mean: {', '.join(similar)}?")
        else:
            print("Chord not found!")
