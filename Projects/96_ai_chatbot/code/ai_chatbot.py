#!/usr/bin/env python3
"""
AI Chatbot - Project 96
Chat with Claude AI right from your Raspberry Pi terminal!
Requires: pip install anthropic
"""

import os
import time

# Try to load .env file
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

# Demo responses for when no API key is set
DEMO_RESPONSES = [
    ("hello", "Hi there! I'm an AI assistant. I can answer questions, tell jokes, help with homework, and much more! (Demo mode)"),
    ("joke",  "Why don't scientists trust atoms? Because they make up everything! 😄 (Demo mode)"),
    ("help",  "I can help you with: answering questions, explaining science, writing stories, solving maths, and having a conversation! (Demo mode)"),
    ("raspberry", "The Raspberry Pi is an amazing tiny computer! It's great for learning coding, building projects, and exploring electronics. (Demo mode)"),
]

def demo_response(message):
    msg_lower = message.lower()
    for keyword, response in DEMO_RESPONSES:
        if keyword in msg_lower:
            return response
    return f"That's an interesting question about '{message}'! In real mode with an API key, Claude would give you a detailed, thoughtful answer. (Demo mode)"

def chat_with_ai(conversation_history, user_message, system_prompt):
    """Send message to Claude API and get response."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")

    if not api_key or api_key == "your-key-here":
        time.sleep(0.5)  # simulate thinking
        return demo_response(user_message), "demo"

    if not API_AVAILABLE:
        return "❌ 'anthropic' library not installed. Run: pip install anthropic", "error"

    try:
        client = anthropic.Anthropic(api_key=api_key)
        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system=system_prompt,
            messages=conversation_history
        )

        ai_message = response.content[0].text
        conversation_history.append({
            "role": "assistant",
            "content": ai_message
        })
        return ai_message, "live"

    except Exception as e:
        return f"❌ API error: {e}", "error"

def choose_personality():
    """Let user pick a chatbot personality."""
    personalities = {
        "1": ("Friendly Helper", "You are a friendly, enthusiastic AI assistant for kids. You explain things clearly, use fun examples, and encourage curiosity. Keep answers concise and engaging."),
        "2": ("Science Tutor", "You are an enthusiastic science tutor. You love explaining how things work, use real-world examples, and make science exciting for young learners."),
        "3": ("Story Buddy", "You are a creative storyteller AI. You love helping kids with creative writing, making up adventures, and bringing imagination to life."),
        "4": ("Homework Helper", "You are a patient homework helper. You guide students through problems step by step, explain concepts clearly, and celebrate their progress."),
        "5": ("Fun Facts Bot", "You are an AI that loves sharing amazing, surprising facts about the world. Every answer includes an interesting fact!"),
    }
    print("\n  Choose your chatbot personality:")
    for key, (name, _) in personalities.items():
        print(f"  [{key}] {name}")
    print("  [6] Custom (you write the personality)")

    choice = input("\n  Choice (1-6): ").strip()

    if choice in personalities:
        name, prompt = personalities[choice]
        print(f"\n  ✅ Chatbot is: {name}")
        return name, prompt
    elif choice == "6":
        print("  Describe the personality (e.g. 'a pirate who loves science'): ", end="")
        custom = input().strip()
        return "Custom Bot", f"You are {custom}. Be fun and helpful!"
    else:
        return "Friendly Helper", personalities["1"][1]

def main():
    print("=" * 50)
    print("  🤖 AI Chatbot - Raspberry Pi Project")
    print("=" * 50)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        print("\n  ⚠️  No API key found — running in DEMO MODE")
        print("  To use real AI:")
        print("  1. Get a key at console.anthropic.com")
        print("  2. Add to .env file: ANTHROPIC_API_KEY=your-key")
        mode = "demo"
    else:
        if not API_AVAILABLE:
            print("\n  ❌ Missing library! Run: pip install anthropic")
            return
        print("\n  ✅ API key found — LIVE AI MODE")
        mode = "live"

    bot_name, system_prompt = choose_personality()

    print(f"\n  💬 Chat with {bot_name}!")
    print("  Type 'quit' to exit, 'clear' to start fresh, 'help' for tips\n")
    print("  " + "─" * 46)

    conversation_history = []
    message_count = 0

    while True:
        try:
            user_input = input("  You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  Goodbye! 👋")
            break

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print(f"\n  Thanks for chatting! You sent {message_count} messages. 👋")
            break

        if user_input.lower() == "clear":
            conversation_history = []
            message_count = 0
            print("  🔄 Conversation cleared — fresh start!\n")
            continue

        if user_input.lower() == "help":
            print("  💡 Tips:")
            print("     - Ask anything! Science, maths, stories, jokes...")
            print("     - 'clear' = start a new conversation")
            print("     - 'quit' = exit the chatbot")
            print("     - The AI remembers what you said earlier in the chat")
            continue

        print(f"\n  {bot_name}: ", end="", flush=True)
        if mode == "live":
            print("thinking...", end="\r", flush=True)
            print(f"  {bot_name}: ", end="", flush=True)

        response, resp_mode = chat_with_ai(
            conversation_history, user_input, system_prompt
        )

        if resp_mode == "demo":
            print(response)
        else:
            # Stream-style word-by-word display for live mode
            words = response.split()
            line_len = 0
            for word in words:
                print(word, end=" ", flush=True)
                line_len += len(word) + 1
                if line_len > 70:
                    print("\n        ", end="")
                    line_len = 0
            print()

        message_count += 1
        print()

if __name__ == "__main__":
    main()
