import random

stories = [
    {
        "title": "A Day at the Zoo",
        "prompts": ["animal", "adjective", "verb (past tense)", "food", "number", "body part"],
        "story": "One day I visited the zoo and saw a {0} {1} {2}. It ate {3} for breakfast and had {4} {5}s. Everyone laughed!"
    },
    {
        "title": "The Space Adventure",
        "prompts": ["planet name", "adjective", "verb", "silly word", "colour", "animal"],
        "story": "Commander Zorg landed on the {0} planet. It was very {1}. She had to {2} the {3} {4} {5} before time ran out!"
    },
    {
        "title": "My Weird School Day",
        "prompts": ["teacher name", "adjective", "school subject", "verb", "food", "number"],
        "story": "Today in school, {0} taught us {1} {2}. We had to {3} for {4} minutes and eat {5} sandwiches. Best day ever!"
    }
]

print("📖 Mad Libs Story Generator!")
print("============================\n")
story = random.choice(stories)
print(f"Story: {story['title']}\n")

answers = []
for prompt in story["prompts"]:
    word = input(f"Give me a {prompt}: ").strip()
    answers.append(word)

print("\n" + "="*40)
print(f"\n📚 {story['title']}\n")
print(story["story"].format(*answers))
print("\n" + "="*40)
