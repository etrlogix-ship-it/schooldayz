questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "How many legs does a spider have?",
        "choices": ["A) 6", "B) 8", "C) 10", "D) 4"],
        "answer": "B"
    },
    {
        "question": "What colour is the sky on a clear day?",
        "choices": ["A) Green", "B) Red", "C) Yellow", "D) Blue"],
        "answer": "D"
    },
    {
        "question": "What planet is closest to the Sun?",
        "choices": ["A) Earth", "B) Venus", "C) Mercury", "D) Mars"],
        "answer": "C"
    },
    {
        "question": "How many sides does a hexagon have?",
        "choices": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "B"
    },
]

score = 0
print("🧠 Welcome to the Trivia Quiz!
")

for i, q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")
    for choice in q["choices"]:
        print(f"  {choice}")
    answer = input("Your answer (A/B/C/D): ").upper().strip()
    if answer == q["answer"]:
        print("✅ Correct!
")
        score += 1
    else:
        print(f"❌ Wrong! The answer was {q['answer']}
")

print(f"🎉 You scored {score} out of {len(questions)}!")
if score == len(questions):
    print("Perfect score! You're a genius! 🌟")
