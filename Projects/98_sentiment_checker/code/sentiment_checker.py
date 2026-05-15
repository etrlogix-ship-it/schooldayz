#!/usr/bin/env python3
"""
AI Sentiment Checker - Project 98
Analyse the emotion/sentiment of any text using AI.
Demo mode uses a simple word-list approach without API.
"""

import os
import json
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

# Demo mode: simple word-based sentiment
POSITIVE_WORDS = {
    "love", "great", "amazing", "awesome", "excellent", "fantastic", "wonderful",
    "brilliant", "happy", "joy", "excited", "perfect", "best", "good", "nice",
    "beautiful", "delightful", "pleased", "thrilled", "superb", "incredible"
}
NEGATIVE_WORDS = {
    "hate", "terrible", "awful", "horrible", "bad", "worst", "disgusting",
    "sad", "angry", "frustrated", "disappointed", "dreadful", "poor", "ugly",
    "annoying", "boring", "useless", "broken", "fail", "failed", "wrong"
}
INTENSIFIERS = {"very", "extremely", "absolutely", "totally", "incredibly", "really"}

SENTIMENT_ICONS = {
    "very positive":  "😄",
    "positive":       "😊",
    "neutral":        "😐",
    "negative":       "😟",
    "very negative":  "😢",
}

def simple_sentiment(text):
    """Rule-based sentiment analysis (no API needed)."""
    words = re.findall(r'\b\w+\b', text.lower())
    pos_count = sum(1 for w in words if w in POSITIVE_WORDS)
    neg_count = sum(1 for w in words if w in NEGATIVE_WORDS)
    intensifier_count = sum(1 for w in words if w in INTENSIFIERS)

    # Boost counts by intensifiers
    multiplier = 1 + (intensifier_count * 0.5)
    pos_score = pos_count * multiplier
    neg_score = neg_count * multiplier

    score = pos_score - neg_score
    total = pos_score + neg_score

    if total == 0:
        sentiment = "neutral"
        confidence = 70
    elif score > 2:
        sentiment = "very positive"
        confidence = min(95, 70 + int(score * 8))
    elif score > 0:
        sentiment = "positive"
        confidence = min(90, 60 + int(score * 10))
    elif score < -2:
        sentiment = "very negative"
        confidence = min(95, 70 + int(abs(score) * 8))
    elif score < 0:
        sentiment = "negative"
        confidence = min(90, 60 + int(abs(score) * 10))
    else:
        sentiment = "neutral"
        confidence = 65

    pos_words_found = [w for w in words if w in POSITIVE_WORDS]
    neg_words_found = [w for w in words if w in NEGATIVE_WORDS]
    reason_parts = []
    if pos_words_found:
        reason_parts.append(f"positive words: {', '.join(pos_words_found[:3])}")
    if neg_words_found:
        reason_parts.append(f"negative words: {', '.join(neg_words_found[:3])}")
    if not reason_parts:
        reason_parts.append("no strong emotion words found")

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "reason": "Demo analysis — found " + "; ".join(reason_parts),
        "mode": "demo"
    }

def ai_sentiment(text):
    """Use Claude AI for accurate sentiment analysis."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        return simple_sentiment(text)
    if not API_AVAILABLE:
        print("  ❌ Install anthropic: pip install anthropic")
        return simple_sentiment(text)

    try:
        client = anthropic.Anthropic(api_key=api_key)
        prompt = f"""Analyse the sentiment of this text and respond with ONLY a JSON object (no other text):

Text: "{text}"

Respond with this exact JSON format:
{{
  "sentiment": "very positive/positive/neutral/negative/very negative",
  "confidence": 0-100,
  "reason": "brief explanation in one sentence",
  "emotions": ["list", "of", "emotions", "detected"]
}}"""

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}]
        )

        result_text = response.content[0].text.strip()
        # Strip markdown code blocks if present
        result_text = re.sub(r"```json|```", "", result_text).strip()
        result = json.loads(result_text)
        result["mode"] = "live"
        return result

    except json.JSONDecodeError:
        return {"sentiment": "neutral", "confidence": 50,
                "reason": "Could not parse AI response", "mode": "error"}
    except Exception as e:
        return {"sentiment": "error", "confidence": 0,
                "reason": str(e), "mode": "error"}

def display_result(text, result):
    """Display sentiment result beautifully."""
    sentiment  = result.get("sentiment", "unknown")
    confidence = result.get("confidence", 0)
    reason     = result.get("reason", "")
    mode       = result.get("mode", "demo")
    emotions   = result.get("emotions", [])
    icon = SENTIMENT_ICONS.get(sentiment, "🤔")

    # Confidence bar
    bar_len  = int(confidence / 5)
    bar_full = "█" * bar_len + "░" * (20 - bar_len)

    print(f"\n  {'─' * 46}")
    print(f"  Text: \"{text[:60]}{'...' if len(text)>60 else ''}\"")
    print(f"  {'─' * 46}")
    print(f"  {icon}  Sentiment:  {sentiment.upper()}")
    print(f"  📊  Confidence: [{bar_full}] {confidence}%")
    print(f"  💭  Reason:     {reason}")
    if emotions:
        print(f"  🎭  Emotions:   {', '.join(emotions)}")
    print(f"  🔧  Mode:       {'Live AI' if mode == 'live' else 'Demo (word-based)'}")
    print()

def bulk_analyse():
    """Analyse multiple texts from a file or list."""
    print("\n  📄 BULK ANALYSIS MODE")
    print("  Enter texts one per line, empty line when done:\n")
    texts = []
    while True:
        line = input("  > ").strip()
        if not line:
            break
        texts.append(line)

    if not texts:
        print("  No texts entered.")
        return

    print(f"\n  Analysing {len(texts)} texts...\n")
    results = []
    for text in texts:
        result = ai_sentiment(text)
        results.append((text, result))
        icon = SENTIMENT_ICONS.get(result["sentiment"], "🤔")
        print(f"  {icon} {result['sentiment']:15s} ({result['confidence']:2d}%) — {text[:40]}")

    # Summary
    sentiments = [r["sentiment"] for _, r in results]
    positive_count = sum(1 for s in sentiments if "positive" in s)
    negative_count = sum(1 for s in sentiments if "negative" in s)
    neutral_count  = len(sentiments) - positive_count - negative_count

    print(f"\n  📊 Summary:")
    print(f"     Positive: {positive_count}/{len(texts)}")
    print(f"     Negative: {negative_count}/{len(texts)}")
    print(f"     Neutral:  {neutral_count}/{len(texts)}")

def main():
    print("=" * 48)
    print("  😊 AI Sentiment Checker - Raspberry Pi")
    print("=" * 48)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "your-key-here":
        print("\n  ⚠️  Demo mode (rule-based analysis)")
        print("  Set ANTHROPIC_API_KEY for AI-powered analysis")
    else:
        print("\n  ✅ Live AI mode")

    print("\n  1. Analyse text one at a time")
    print("  2. Bulk analysis (multiple texts)")
    print("  3. See demo examples")

    choice = input("\n  Choice (1-3): ").strip()

    if choice == "2":
        bulk_analyse()

    elif choice == "3":
        examples = [
            "I absolutely love this project, it's the best thing ever!",
            "This is broken and completely useless. I'm so frustrated.",
            "The temperature today is 18 degrees Celsius.",
            "I'm a bit disappointed but I'll give it another try.",
            "WOW! This is incredible! I can't believe how amazing this is!"
        ]
        print("\n  📝 Demo examples:\n")
        for text in examples:
            result = ai_sentiment(text)
            display_result(text, result)

    else:
        print("\n  Type any text to analyse sentiment. 'quit' to exit.\n")
        while True:
            try:
                text = input("  Enter text: ").strip()
                if not text:
                    continue
                if text.lower() in ("quit", "q", "exit"):
                    break
                result = ai_sentiment(text)
                display_result(text, result)
            except (KeyboardInterrupt, EOFError):
                print()
                break

    print("  Goodbye! 😊")

if __name__ == "__main__":
    main()
