import random

def play_game():
    print("🎮 Welcome to Guess the Number!")
    print("I am thinking of a number between 1 and 100.")
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts+1}/{max_attempts} — Your guess: "))
        except ValueError:
            print("Please enter a whole number!")
            continue

        attempts += 1

        if guess < secret:
            print("📈 Too low! Try higher.")
        elif guess > secret:
            print("📉 Too high! Try lower.")
        else:
            print(f"🎉 Correct! You got it in {attempts} attempts!")
            return

    print(f"😢 Out of attempts! The number was {secret}.")

while True:
    play_game()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break
