import random

word_lists = [
    ("Twinkle Little Star", ["Twinkle", "Diamond", "Sky", "Star", "Wonder"]),
    ("Old MacDonald", ["Farm", "Duck", "Cow", "Quack", "MacDonald"]),
    ("Row Your Boat", ["Boat", "Stream", "Dream", "Life", "Row"]),
    ("Happy Birthday", ["Birthday", "Happy", "You", "Dear", "Song"]),
]

print("Lyric Scrambler Game!")
print("=====================")
print("Unscramble the words to guess the song!")
score = 0

random.shuffle(word_lists)
for title, words in word_lists[:4]:
    scrambled = words[:]
    random.shuffle(scrambled)
    while scrambled == words:
        random.shuffle(scrambled)
    print(f"\nScrambled words: {' | '.join(scrambled)}")
    guess = input("What song is this from? ").strip()
    if guess.lower() in title.lower() or title.lower() in guess.lower():
        print(f"Correct! It was: {title}"); score += 1
    else:
        print(f"Wrong! It was: {title}")

print(f"\nFinal score: {score}/{len(word_lists[:4])}")
