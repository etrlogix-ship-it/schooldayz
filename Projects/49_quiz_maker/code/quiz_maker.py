import json, os

FILE = "my_quiz.json"
def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return []
def save(q):
    with open(FILE,"w") as f: json.dump(q, f, indent=2)

questions = load()

print("Quiz Maker")
print("==========")
while True:
    print("\n1) Add question  2) Take quiz  3) List questions  4) Clear all  5) Quit")
    choice = input("Choose: ")
    if choice == "1":
        q = input("Question: ").strip()
        options = []
        for i in range(1, 5):
            o = input(f"Option {i}: ").strip()
            options.append(o)
        correct = input("Correct option number (1-4): ").strip()
        try:
            correct_idx = int(correct) - 1
            if 0 <= correct_idx <= 3:
                questions.append({"q": q, "options": options, "answer": correct_idx})
                save(questions)
                print("Question added!")
            else:
                print("Invalid option number!")
        except ValueError:
            print("Invalid!")
    elif choice == "2":
        if not questions:
            print("No questions yet!")
            continue
        score = 0
        for i, q in enumerate(questions):
            print(f"\nQ{i+1}: {q['q']}")
            for j, opt in enumerate(q["options"]):
                print(f"  {j+1}. {opt}")
            try:
                ans = int(input("Your answer (1-4): ")) - 1
                if ans == q["answer"]:
                    print("Correct!"); score += 1
                else:
                    print(f"Wrong! The answer was: {q['options'][q['answer']]}")
            except ValueError:
                print("Invalid!")
        print(f"\nScore: {score}/{len(questions)}")
    elif choice == "3":
        for i, q in enumerate(questions):
            print(f"  {i+1}. {q['q']}")
    elif choice == "4":
        questions = []; save(questions)
        print("Cleared!")
    elif choice == "5":
        break
