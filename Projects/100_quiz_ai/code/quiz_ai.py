#!/usr/bin/env python3
"""
AI Quiz Master - Project 100 🏆
The grand finale! An AI generates fresh quiz questions on any topic.
Every game is different!
"""

import os
import json
import time
import random
import re

def load_env():
    env_file = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip().strip('"')

load_env()

try:
    import anthropic
    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False

# Built-in demo questions about Raspberry Pi and coding
DEMO_QUESTIONS = [
    {
        "question": "What programming language is most commonly used on the Raspberry Pi?",
        "options": ["A) Java", "B) Python", "C) C++", "D) HTML"],
        "answer": "B",
        "explanation": "Python is the official language of the Raspberry Pi and is perfect for beginners!"
    },
    {
        "question": "What does GPIO stand for?",
        "options": ["A) General Purpose Input/Output", "B) Graphics Processing Interface Output",
                    "C) Global Program Input Operations", "D) Great Pi Input/Output"],
        "answer": "A",
        "explanation": "GPIO pins let the Raspberry Pi talk to the physical world — like LEDs and buttons!"
    },
    {
        "question": "What does an LED stand for?",
        "options": ["A) Light Emitting Device", "B) Low Energy Display",
                    "C) Light Emitting Diode", "D) Large Electronic Display"],
        "answer": "C",
        "explanation": "LEDs are efficient light sources that only work in one direction — that's what 'diode' means."
    },
    {
        "question": "What resistor value should you typically use with an LED on a Raspberry Pi?",
        "options": ["A) 10Ω", "B) 100Ω", "C) 330Ω", "D) 10,000Ω"],
        "answer": "C",
        "explanation": "A 330Ω resistor limits current to a safe level for both the LED and the Pi's GPIO pin."
    },
    {
        "question": "Which command installs Python packages on a Raspberry Pi?",
        "options": ["A) install python", "B) pip install", "C) python get", "D) apt-get python"],
        "answer": "B",
        "explanation": "pip is Python's package manager — use 'pip install package_name' to add new libraries!"
    },
    {
        "question": "What is a 'for loop' in Python used for?",
        "options": ["A) Making decisions", "B) Repeating code a set number of times",
                    "C) Storing data", "D) Connecting to the internet"],
        "answer": "B",
        "explanation": "A for loop lets you repeat a block of code — great for making an LED blink 10 times!"
    },
    {
        "question": "Which Raspberry Pi GPIO mode uses pin numbers from the chip itself?",
        "options": ["A) BOARD mode", "B) PHYSICAL mode", "C) BCM mode", "D) GPIO mode"],
        "answer": "C",
        "explanation": "BCM mode (Broadcom) uses the chip's pin numbers. BOARD mode uses the physical connector numbers."
    },
    {
        "question": "What does this Python code do? `time.sleep(1)`",
        "options": ["A) Stops the program forever", "B) Pauses for 1 second",
                    "C) Runs 1 time", "D) Shows the time"],
        "answer": "B",
        "explanation": "time.sleep() pauses execution for the number of seconds you specify — great for timing blinks!"
    },
]

def generate_ai_questions(topic, difficulty, num_questions=5):
    """Ask Claude to generate quiz questions on any topic."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        return None, "no_key"
    if not API_AVAILABLE:
        return None, "no_lib"

    try:
        client = anthropic.Anthropic(api_key=api_key)
        prompt = f"""Generate {num_questions} multiple choice quiz questions about "{topic}" at {difficulty} difficulty level for children aged 8-14.

Respond with ONLY a JSON array (no other text, no markdown backticks):
[
  {{
    "question": "The question text here?",
    "options": ["A) First option", "B) Second option", "C) Third option", "D) Fourth option"],
    "answer": "A",
    "explanation": "Brief explanation of why this is correct (1-2 sentences)"
  }}
]

Rules:
- Questions should be interesting and age-appropriate
- One clear correct answer per question
- {difficulty} difficulty: {"use simple, well-known facts" if difficulty=="easy" else "use moderately challenging facts" if difficulty=="medium" else "use detailed, challenging facts"}
- Make the wrong answers plausible but clearly incorrect to someone who knows the topic"""

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )

        result_text = response.content[0].text.strip()
        # Remove any markdown code blocks
        result_text = re.sub(r"```json|```", "", result_text).strip()
        questions = json.loads(result_text)
        return questions, "live"

    except json.JSONDecodeError as e:
        return None, f"parse_error: {e}"
    except Exception as e:
        return None, f"api_error: {e}"

def run_quiz(questions, topic):
    """Run through a list of quiz questions."""
    score = 0
    total = len(questions)
    wrong_answers = []

    print(f"\n  📝 Quiz: {topic} ({total} questions)")
    print("  " + "═" * 44)

    for i, q in enumerate(questions, 1):
        print(f"\n  Question {i}/{total}:")
        print(f"  {q['question']}\n")
        for option in q["options"]:
            print(f"  {option}")

        # Get answer
        while True:
            answer = input("\n  Your answer (A/B/C/D): ").strip().upper()
            if answer in ("A", "B", "C", "D"):
                break
            print("  Please enter A, B, C, or D")

        correct = q["answer"].upper()
        if answer == correct:
            print(f"\n  ✅ CORRECT! 🎉")
            score += 1
        else:
            print(f"\n  ❌ Wrong — the answer was {correct}")
            wrong_answers.append(q)

        explanation = q.get("explanation", "")
        if explanation:
            print(f"  💡 {explanation}")

        if i < total:
            input("\n  Press Enter for next question...")

    return score, total, wrong_answers

def show_score(score, total, topic):
    """Show final score with rating."""
    pct = score / total * 100
    print(f"\n  {'═' * 44}")
    print(f"  🏆 QUIZ COMPLETE: {topic}")
    print(f"  {'═' * 44}")
    print(f"  Score: {score}/{total}  ({pct:.0f}%)")

    # Star rating
    if pct == 100:   rating = "⭐⭐⭐ PERFECT SCORE! Amazing! 🎊"
    elif pct >= 80:  rating = "⭐⭐⭐ Excellent work!"
    elif pct >= 60:  rating = "⭐⭐ Good job!"
    elif pct >= 40:  rating = "⭐ Keep practising!"
    else:            rating = "📚 Time to do some research!"

    print(f"  Rating: {rating}")

    # Progress bar
    filled = int(pct / 5)
    bar = "█" * filled + "░" * (20 - filled)
    print(f"  [{bar}] {pct:.0f}%")

def main():
    print("╔" + "═" * 48 + "╗")
    print("║  🏆 AI QUIZ MASTER — Raspberry Pi          ║")
    print("║     Project 100 — The Grand Finale!        ║")
    print("╚" + "═" * 48 + "╝")

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        print("\n  ⚠️  Demo mode — using built-in questions")
        print("  Set ANTHROPIC_API_KEY for AI-generated questions on ANY topic!\n")
        use_demo = True
    else:
        if not API_AVAILABLE:
            print("  ❌ Run: pip install anthropic")
            return
        print("\n  ✅ Live AI mode — questions on any topic!\n")
        use_demo = False

    keep_playing = True
    total_score = 0
    total_questions = 0
    games_played = 0

    while keep_playing:
        if use_demo:
            topic = "Raspberry Pi & Coding"
            difficulty = "mixed"
            questions = random.sample(DEMO_QUESTIONS, min(5, len(DEMO_QUESTIONS)))
            source = "demo"
        else:
            print("  🌍 What topic would you like questions about?")
            print("  Examples: space, dinosaurs, football, Harry Potter, science...")
            topic = input("  Topic: ").strip()
            if not topic:
                topic = "general knowledge"

            print("\n  📊 Choose difficulty:")
            print("  [1] Easy   — simple facts")
            print("  [2] Medium — moderate challenge")
            print("  [3] Hard   — really tough!")
            d_choice = input("  Choice (1-3): ").strip()
            difficulty = {"1": "easy", "2": "medium", "3": "hard"}.get(d_choice, "medium")

            num_q = input("\n  How many questions? (3-10, default 5): ").strip()
            try:
                num_q = max(3, min(10, int(num_q)))
            except:
                num_q = 5

            print(f"\n  🤔 Generating {num_q} {difficulty} questions about '{topic}'...", end="", flush=True)
            questions, source = generate_ai_questions(topic, difficulty, num_q)

            if questions is None:
                print(f"\n  ⚠️  Couldn't generate questions ({source}). Using demo questions.")
                questions = random.sample(DEMO_QUESTIONS, 5)
                topic = "Raspberry Pi & Coding"
                source = "demo"
            else:
                print(" Done! ✨")

        score, total, wrong = run_quiz(questions, topic)
        show_score(score, total, topic)

        total_score     += score
        total_questions += total
        games_played    += 1

        # Review wrong answers
        if wrong:
            print(f"\n  📚 Review your {len(wrong)} wrong answer(s)? (y/n): ", end="")
            if input().strip().lower() == 'y':
                print("\n  Wrong answers:\n")
                for q in wrong:
                    print(f"  Q: {q['question']}")
                    print(f"  ✅ Correct: {q['answer']} — {q['explanation']}\n")

        print(f"\n  Overall: {total_score}/{total_questions} across {games_played} game(s)")
        print("  Play again? (y/n): ", end="")
        keep_playing = input().strip().lower() == 'y'

    print("\n╔" + "═" * 48 + "╗")
    print("║  🎉 CONGRATULATIONS!                       ║")
    print("║                                            ║")
    print("║  You've completed all 100 Raspberry Pi     ║")
    print("║  projects! You're officially a Pi expert!  ║")
    print("║                                            ║")
    print("║  🚀 Now go build something amazing!        ║")
    print("╚" + "═" * 48 + "╝\n")

if __name__ == "__main__":
    main()
