import random

questions = [
    ("Who sang 'Thriller' in 1982?", ["Michael Jackson","Prince","David Bowie","Elvis"], "Michael Jackson"),
    ("What instrument has black and white keys?", ["Guitar","Piano","Violin","Drum"], "Piano"),
    ("How many strings does a standard guitar have?", ["4","5","6","8"], "6"),
    ("Which band wrote 'Bohemian Rhapsody'?", ["The Beatles","Queen","Led Zeppelin","ABBA"], "Queen"),
    ("What is the fastest instrument to typically play a melody?", ["Tuba","Double Bass","Violin","Trombone"], "Violin"),
    ("In music, what does 'forte' mean?", ["Slow","Loud","Soft","Fast"], "Loud"),
    ("How many musicians are in a quartet?", ["2","3","4","5"], "4"),
    ("What country does the samba dance originate from?", ["Argentina","Cuba","Brazil","Mexico"], "Brazil"),
    ("What is the lowest male singing voice called?", ["Tenor","Baritone","Bass","Alto"], "Bass"),
    ("How many notes are in a standard musical scale?", ["5","6","7","8"], "7"),
]

print("Music History Quiz!")
print("===================")
random.shuffle(questions)
score = 0

for i, (q, opts, ans) in enumerate(questions[:8]):
    random.shuffle(opts)
    print(f"\nQ{i+1}: {q}")
    for j, o in enumerate(opts): print(f"  {j+1}. {o}")
    try:
        user = int(input("Answer (1-4): ")) - 1
        if opts[user] == ans:
            print("Correct!"); score += 1
        else:
            print(f"Wrong! Answer: {ans}")
    except (ValueError, IndexError):
        print(f"Skipped! Answer: {ans}")

print(f"\nFinal score: {score}/8")
