#!/usr/bin/env python3
"""
AI Story Generator - Project 99
Give the AI a hero, setting, and challenge — get a unique story!
"""

import os
import random
import time

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

# Demo story templates
DEMO_OPENINGS = [
    "Once upon a time, in {setting}, there lived {hero}.",
    "It was an ordinary day in {setting} when {hero} discovered something extraordinary.",
    "Nobody in {setting} had ever seen anything quite like {hero} before.",
    "Deep in the heart of {setting}, {hero} was about to have the biggest adventure of their life.",
]

DEMO_MIDDLES = [
    "The challenge was clear: {challenge}. But no one had ever succeeded before.",
    "When faced with the task to {challenge}, {hero} knew this would be no easy journey.",
    "To {challenge} seemed impossible — but {hero} had a secret that nobody knew about.",
]

DEMO_ENDINGS = [
    "In the end, {hero} discovered that the real answer had been inside them all along. And {setting} was never the same again.",
    "With courage and cleverness, {hero} managed to {challenge} — and earned the admiration of everyone in {setting}.",
    "The adventure wasn't perfect, and {hero} made mistakes along the way. But that's what made the story of {setting} so worth telling.",
]

STORY_GENRES = {
    "1": "adventure",
    "2": "mystery",
    "3": "funny/comedy",
    "4": "scary (mild)",
    "5": "science fiction",
}

RANDOM_HEROES = [
    "a robot who wants to be a chef",
    "a dragon who's afraid of fire",
    "a young wizard who keeps getting spells backwards",
    "a mermaid who wants to explore land",
    "a tiny mouse who wants to be a knight",
]

RANDOM_SETTINGS = [
    "a floating city in the clouds",
    "an underwater kingdom",
    "a forest where the trees can talk",
    "a chocolate-covered planet in outer space",
    "a school for monsters",
]

RANDOM_CHALLENGES = [
    "must find a lost magical object before sunrise",
    "has to make a new friend who seems very different",
    "needs to solve a mystery that everyone else has given up on",
    "must win a competition with only one day to prepare",
    "has to save their home from being destroyed",
]

def demo_story(hero, setting, challenge, genre):
    """Generate a template-based story without AI."""
    opening = random.choice(DEMO_OPENINGS).format(hero=hero, setting=setting, challenge=challenge)
    middle  = random.choice(DEMO_MIDDLES).format(hero=hero, setting=setting, challenge=challenge)
    ending  = random.choice(DEMO_ENDINGS).format(hero=hero, setting=setting, challenge=challenge)

    story = f"""{opening}

Life was unusual there, but {hero} had always managed to fit in — mostly. 
The real trouble started on a {["stormy", "sunny", "foggy", "starlit"][random.randint(0,3)]} day 
when everything changed.

{middle}

{hero} thought carefully. They remembered something an old friend had once said: 
"The answer is never as far away as it seems." 
With new determination, {hero} set off into {setting} with a plan.

There were obstacles, of course. There always are in a good {genre} story.
But {hero} faced each one with creativity and heart.

{ending}

THE END

[✨ This was a demo story! Connect your API key for unique AI-written stories every time.]"""

    return story

def ai_story(hero, setting, challenge, genre, length="medium"):
    """Generate a story using Claude AI."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        return demo_story(hero, setting, challenge, genre), "demo"
    if not API_AVAILABLE:
        return demo_story(hero, setting, challenge, genre), "demo"

    word_counts = {"short": "150-200", "medium": "250-350", "long": "450-550"}
    word_count  = word_counts.get(length, "250-350")

    try:
        client = anthropic.Anthropic(api_key=api_key)
        prompt = f"""Write a {genre} children's story with these ingredients:
- Hero: {hero}
- Setting: {setting}  
- Challenge: {challenge}

The story should be {word_count} words, age-appropriate for 8-12 year olds, 
have a clear beginning/middle/end, and include a satisfying resolution.
Write only the story — no title, no notes."""

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=700,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text, "live"
    except Exception as e:
        return demo_story(hero, setting, challenge, genre), "demo"

def print_story(text):
    """Print story with nice word wrapping."""
    paragraphs = text.strip().split("\n\n")
    for para in paragraphs:
        words = para.split()
        line = "  "
        for word in words:
            if len(line) + len(word) + 1 > 70:
                print(line)
                line = "  " + word + " "
            else:
                line += word + " "
        if line.strip():
            print(line)
        print()

def get_ingredients():
    """Interactively gather story ingredients from the user."""
    print("\n  Let's gather the story ingredients!\n")

    # Hero
    print(f"  🦸 Who is the hero of the story?")
    print(f"     (e.g. {random.choice(RANDOM_HEROES)})")
    print(f"     Or press Enter for a random hero: ", end="")
    hero = input().strip()
    if not hero:
        hero = random.choice(RANDOM_HEROES)
        print(f"     → Using: {hero}")

    # Setting
    print(f"\n  🌍 Where does the story take place?")
    print(f"     (e.g. {random.choice(RANDOM_SETTINGS)})")
    print(f"     Or press Enter for random setting: ", end="")
    setting = input().strip()
    if not setting:
        setting = random.choice(RANDOM_SETTINGS)
        print(f"     → Using: {setting}")

    # Challenge
    print(f"\n  ⚔️  What is the hero's challenge or goal?")
    print(f"     (e.g. {random.choice(RANDOM_CHALLENGES)})")
    print(f"     Or press Enter for random challenge: ", end="")
    challenge = input().strip()
    if not challenge:
        challenge = random.choice(RANDOM_CHALLENGES)
        print(f"     → Using: {challenge}")

    # Genre
    print(f"\n  📚 What kind of story?")
    for key, genre in STORY_GENRES.items():
        print(f"     [{key}] {genre}")
    g_choice = input("     Choice (1-5, default=1): ").strip()
    genre = STORY_GENRES.get(g_choice, "adventure")

    return hero, setting, challenge, genre

def main():
    print("=" * 48)
    print("  📖 AI Story Generator - Raspberry Pi")
    print("=" * 48)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        print("\n  ⚠️  Demo mode (template stories)")
    else:
        print("\n  ✅ Live AI mode — unique stories!")
        if not API_AVAILABLE:
            print("  ❌ Run: pip install anthropic")
            return

    keep_going = True
    while keep_going:
        hero, setting, challenge, genre = get_ingredients()

        print(f"\n  📝 Story ingredients:")
        print(f"     Hero:      {hero}")
        print(f"     Setting:   {setting}")
        print(f"     Challenge: {challenge}")
        print(f"     Genre:     {genre}")

        length = input("\n  Story length? (short/medium/long, default=medium): ").strip().lower()
        if length not in ("short", "long"):
            length = "medium"

        print(f"\n  ✨ Writing your story...\n")
        print("  " + "═" * 44)

        story, mode = ai_story(hero, setting, challenge, genre, length)

        if mode == "live":
            # Simulate typing effect
            for char in story:
                print(char, end="", flush=True)
                if char in ".!?":
                    time.sleep(0.05)
                elif char == "\n":
                    time.sleep(0.02)
        else:
            print_story(story)

        print("  " + "═" * 44)
        print(f"\n  Mode: {'✨ AI-generated' if mode == 'live' else '📝 Demo template'}")

        print("\n  Write another story? (y/n): ", end="")
        again = input().strip().lower()
        keep_going = again == "y"

    print("\n  The end! Keep writing your own stories too! 📖")

if __name__ == "__main__":
    main()
