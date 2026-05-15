# 96 🤖 AI Chatbot

**Category:** 🧠 AI & Cool Tech  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 20 minutes

## What You'll Make
Build your own AI chatbot powered by Claude AI! You can have real conversations, ask questions, get help with homework, or just chat. This is a real AI — not just canned responses!

## What You'll Learn
- How to call an AI API from Python
- Working with HTTP requests
- Building a conversational interface
- How large language models work

## Parts You'll Need
Just your Raspberry Pi and internet connection! No extra hardware needed.

## Setup

### Step 1 — Get an API key
1. Visit [console.anthropic.com](https://console.anthropic.com)
2. Sign up for a free account
3. Create an API key

### Step 2 — Install the library
```bash
pip install anthropic
```

### Step 3 — Set your API key
```bash
export ANTHROPIC_API_KEY="your-key-here"
```
Or create a file called `.env` in the code folder with:
```
ANTHROPIC_API_KEY=your-key-here
```

### Step 4 — Run it!
```bash
python3 ai_chatbot.py
```

## What Can You Ask?
- "Explain how rainbows form"
- "Help me with my maths homework"
- "Tell me a joke"
- "What's the capital of Brazil?"
- "Write me a short poem about my cat"

## Demo Mode
Don't have an API key yet? Run in demo mode — it shows pre-written responses so you can see how it works!

## How It Works
Your message → sent to Claude AI via the internet → Claude thinks → sends back an answer → displayed on screen
