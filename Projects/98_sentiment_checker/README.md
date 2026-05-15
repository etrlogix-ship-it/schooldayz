# 98 😊 AI Sentiment Checker

**Category:** 🧠 AI & Cool Tech  
**Difficulty:** ⭐ Beginner  
**Time:** 15 minutes

## What You'll Make
Type any sentence and the AI will tell you if it's positive 😊, negative 😢, or neutral 😐! It can also tell you *why* and how confident it is. This is how companies analyse customer reviews automatically!

## What You'll Learn
- Sentiment analysis (a real AI technique)
- How AI classifies text
- Natural language processing basics

## Parts You'll Need
Just your Raspberry Pi and internet connection!

## Setup

```bash
pip install anthropic
export ANTHROPIC_API_KEY="your-key-here"
python3 sentiment_checker.py
```

## What Is Sentiment Analysis?
Sentiment analysis is a type of AI that reads text and figures out whether the writer is happy, sad, angry, or neutral. Companies use it to:
- Automatically read thousands of customer reviews
- Monitor social media for complaints
- Understand how people feel about their products

## Example
```
Text: "I absolutely love this new game, it's amazing!"
Result: 😊 VERY POSITIVE (confidence: 98%)
Reason: Uses strong positive words like "absolutely love" and "amazing"

Text: "The weather is cloudy today."
Result: 😐 NEUTRAL (confidence: 85%)
Reason: Factual statement with no emotional language
```

## Demo Mode
Works without an API key — shows rule-based sentiment analysis using a word list so you can see the concept!
