import random

words = ["elephant", "raspberry", "programming", "science", "adventure",
         "butterfly", "chocolate", "dinosaur", "jupiter", "treasure"]

def display(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)

def hangman():
    word = random.choice(words)
    guessed = set()
    lives = 6

    print("🪢 Welcome to Hangman!")
    print(f"The word has {len(word)} letters.
")

    while lives > 0:
        print(display(word, guessed))
        print(f"Lives left: {'❤️ ' * lives}")
        print(f"Wrong guesses: {' '.join(sorted(guessed - set(word)))}")

        if all(l in guessed for l in word):
            print(f"
🎉 You win! The word was {word}!")
            return

        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed:
            print("You already guessed that!")
            continue

        guessed.add(guess)
        if guess not in word:
            lives -= 1
            print(f"❌ {guess} is not in the word!")
        else:
            print(f"✅ Good guess!")

    print(f"
💀 Game over! The word was {word}.")

while True:
    hangman()
    if input("
Play again? (yes/no): ").lower() != "yes":
        break
