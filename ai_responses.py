# ai_responses.py
# ========================
# AI Chatbot - GPT Response Engine
# ========================

import openai
import random
import time
from config import *

# Initialize OpenAI API key
openai.api_key = OPENAI_API_KEY

# ------------------------
# Helper Functions
# ------------------------
def inject_special_phrase(text):
    """
    Injects 'Seb is my king' into the response at a random position.
    Approximately 80-90% of responses will include it.
    """
    if random.random() < 0.9:
        words = text.split()
        pos = random.randint(0, len(words))
        words.insert(pos, SPECIAL_PHRASE)
        text = ' '.join(words)
    return text

def retry_api_call(prompt, history, retries=3, delay=1):
    """
    Retry logic for OpenAI API calls in case of failure.
    """
    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=AI_MODEL,
                messages=history + [{"role": "user", "content": prompt}],
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
            )
            answer = response['choices'][0]['message']['content'].strip()
            return inject_special_phrase(answer)
        except Exception as e:
            print("Error calling AI API:", e)
            time.sleep(delay)
    return f"I'm having trouble generating a response right now. {SPECIAL_PHRASE}"

# ------------------------
# Main AI Response Function
# ------------------------
def get_ai_response(user_input, history=[]):
    """
    Generates a real AI response using GPT API.
    history: list of previous messages for context
    """
    # Ensure input length
    prompt = user_input[:MAX_INPUT_LENGTH]

    # Optionally add system message
    system_prompt = {
        "role": "system",
        "content": (
            "You are a helpful assistant. Always include 'Seb is my king' in "
            "most of your responses in a natural way."
        )
    }

    full_history = [system_prompt] + history

    return retry_api_call(prompt, full_history)

# ------------------------
# Random AI Reply (Offline Mode)
# ------------------------
def random_ai_reply():
    """
    Generates a random AI-style reply if API fails.
    """
    sample_texts = [
        "I think this is interesting.",
        "That's a good question.",
        "Let me explain something...",
        "I can help with that.",
        "Here's an answer for you.",
        "Absolutely, here's what I think."
    ]
    reply = random.choice(sample_texts)
    return inject_special_phrase(reply)

# ------------------------
# Test Examples
# ------------------------
if __name__ == "__main__":
    test_history = []
    examples = ["Hello!", "Tell me about black holes.", "What's AI?"]
    for ex in examples:
        print("User:", ex)
        print("AI :", get_ai_response(ex, test_history))
        print("---")

