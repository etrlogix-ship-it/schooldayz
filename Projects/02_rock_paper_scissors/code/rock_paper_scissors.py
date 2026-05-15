import random

choices = ["rock", "paper", "scissors"]
wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

player_score = 0
pi_score = 0

print("✂️ Rock, Paper, Scissors!")
print("Type rock, paper, or scissors. Type quit to stop.
")

while True:
    player = input("Your choice: ").lower().strip()
    if player == "quit":
        break
    if player not in choices:
        print("Invalid choice! Try rock, paper, or scissors.")
        continue

    pi = random.choice(choices)
    print(f"Pi chose: {pi}")

    if player == pi:
        print("🤝 It's a tie!")
    elif wins[player] == pi:
        print("🏆 You win!")
        player_score += 1
    else:
        print("🤖 Pi wins!")
        pi_score += 1

    print(f"Score — You: {player_score} | Pi: {pi_score}
")

print(f"Final Score — You: {player_score} | Pi: {pi_score}")
print("Thanks for playing!")
