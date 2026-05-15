import random

words = [
    ("Ephemeral", "adj.", "Lasting for a very short time.", "The morning dew is ephemeral, gone by sunrise."),
    ("Serendipity", "n.", "Finding something good without looking for it.", "Finding a coin on the pavement — pure serendipity!"),
    ("Perspicacious", "adj.", "Having good judgement and understanding.", "The perspicacious student solved the puzzle in seconds."),
    ("Ubiquitous", "adj.", "Seeming to be everywhere at once.", "Smartphones have become ubiquitous in modern life."),
    ("Mellifluous", "adj.", "A pleasant, smooth, musical sound.", "The singer had a mellifluous voice."),
    ("Petrichor", "n.", "The pleasant smell after rain.", "The petrichor after the storm was wonderful."),
    ("Loquacious", "adj.", "Tending to talk a great deal.", "My loquacious friend never stops chatting!"),
    ("Sonder", "n.", "The realisation that others have complex lives too.", "Sonder hit me while people-watching at the park."),
    ("Quixotic", "adj.", "Extremely idealistic, unrealistic.", "Building a rocket in the garage was a quixotic dream."),
    ("Incandescent", "adj.", "Emitting light as a result of being heated; brilliant.", "Her incandescent smile lit up the room."),
]

print("Word of the Day!")
print("================")
word, pos, definition, example = random.choice(words)
print(f"\nToday\'s word: {word} ({pos})")
print(f"\nDefinition: {definition}")
print(f"\nExample: \"{example}\"")
print("\nTry using this word in a sentence today!")
input("\nPress Enter to see another word...")
for _ in range(3):
    word, pos, definition, example = random.choice(words)
    print(f"\n{word} ({pos}) — {definition}")
    print(f"  Example: {example}")
