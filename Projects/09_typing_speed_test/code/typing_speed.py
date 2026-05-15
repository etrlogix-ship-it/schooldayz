import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Raspberry Pi is a tiny and affordable computer",
    "Python is a great programming language for beginners",
    "Learning to code is a superpower for the future",
    "The stars shine brightly in the night sky above us",
    "A journey of a thousand miles begins with a single step",
]

print("⌨️  Typing Speed Test!")
print("======================")
print("Type the sentence as fast and accurately as you can.\n")

while True:
    sentence = random.choice(sentences)
    print(f"Type this:\n\n  👉 {sentence}\n")
    input("Press Enter when ready...")

    start = time.time()
    typed = input("\nGo! --> ")
    elapsed = time.time() - start

    words = len(sentence.split())
    wpm = round((words / elapsed) * 60)

    # Accuracy
    correct = sum(a == b for a, b in zip(typed, sentence))
    accuracy = round((correct / len(sentence)) * 100)

    print(f"\n⏱️  Time: {elapsed:.2f} seconds")
    print(f"🚀 Speed: {wpm} WPM")
    print(f"✅ Accuracy: {accuracy}%")

    if typed == sentence:
        print("🌟 Perfect typing!")
    else:
        print("Keep practising!")

    if input("\nTry again? (yes/no): ").lower() != "yes":
        break
