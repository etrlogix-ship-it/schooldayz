# 99 📖 AI Story Generator

**Category:** 🧠 AI & Cool Tech  
**Difficulty:** ⭐ Beginner  
**Time:** 15 minutes

## What You'll Make
A magical story machine! You give it a character, a setting, and a problem — and the AI writes a unique story just for you. Every story is different! Great for bedtime stories or creative writing inspiration.

## What You'll Learn
- Creative AI text generation
- Prompt engineering (how to ask AI for specific things)
- How changing prompts changes AI output

## Parts You'll Need
Just your Raspberry Pi and internet connection!

## Setup

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
python3 story_ai.py
```

## Story Ingredients
You provide:
- **A hero** (e.g. "a brave dragon", "a shy robot", "a girl who can talk to plants")
- **A setting** (e.g. "an underwater city", "a space station", "medieval village")
- **A challenge** (e.g. "must find a lost treasure", "needs to make a new friend")

The AI writes the rest!

## Example
```
Hero: a tiny fairy who hates flying
Setting: a giant library with books that come alive
Challenge: has to find the most important book before midnight

Story: In the towering Library of Whispers, there lived a tiny fairy
named Bramble who had one unusual problem for a fairy — she absolutely
refused to fly...
```

## Demo Mode
Creates template-based stories without needing an API key, showing you how the story structure works!
