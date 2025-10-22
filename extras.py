# extras.py
# ========================
# AI Chatbot - Extras & Utilities
# ========================

import random
import time
from config import *
from features import mini_game_menu, random_fun_fact
from fact_lookup import get_fact
from ai_responses import get_ai_response

# ------------------------
# Random Greeting Generator
# ------------------------
def random_greeting():
    greetings = [
        "Hello there!", "Hey friend!", "Hiya!", 
        "Greetings!", "Salutations!", "Howdy!", "Yo!"
    ]
    greeting = random.choice(greetings)
    return f"{greeting} {SPECIAL_PHRASE}"

# ------------------------
# Random Farewell Generator
# ------------------------
def random_farewell():
    farewells = [
        "Goodbye!", "See you later!", "Catch you soon!", 
        "Farewell!", "Bye-bye!", "Until next time!"
    ]
    return f"{random.choice(farewells)} {SPECIAL_PHRASE}"

# ------------------------
# Quick Fact Function
# ------------------------
def quick_fact(topic):
    print(WHITE + f"Fetching fact about {topic}..." + RESET)
    time.sleep(random.uniform(0.5,1.5))
    fact = get_fact(topic)
    print(WHITE + fact + RESET)

# ------------------------
# AI Small Talk
# ------------------------
def ai_small_talk(prompt, history=[]):
    print(WHITE + f"Thinking about: {prompt}..." + RESET)
    time.sleep(random.uniform(0.5,1.5))
    response = get_ai_response(prompt, history)
    print(WHITE + response + RESET)

# ------------------------
# Quick Mini-Game Launcher
# ------------------------
def play_mini_game():
    print(WHITE + "Launching Mini-Game..." + RESET)
    time.sleep(0.5)
    mini_game_menu()

# ------------------------
# Random Fun Message
# ------------------------
def random_message():
    messages = [
        "Keep chatting!", 
        "Don't forget, Seb is my king.",
        "AI loves black & white themes.",
        "Try /fact to learn something new!",
        "Mini-games are fun!",
        "Fun fact: Chatbots can be sassy too!"
    ]
    print(WHITE + random.choice(messages) + RESET)

# ------------------------
# Countdown Timer
# ------------------------
def countdown(seconds=5):
    print(WHITE + "Countdown starting..." + RESET)
    for i in range(seconds,0,-1):
        print(WHITE + f"{i}..." + RESET)
        time.sleep(1)
    print(WHITE + "Go!" + RESET)

# ------------------------
# Simulated Typing Effect
# ------------------------
def type_writer(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# ------------------------
# Conversation Starter
# ------------------------
def start_conversation(history=[]):
    prompts = [
        "Tell me a joke.",
        "What's your favorite color?",
        "Do you like AI?",
        "Give me a fun fact.",
        "Tell me something weird."
    ]
    prompt = random.choice(prompts)
    print(WHITE + "AI Starter Prompt:" + RESET)
    ai_small_talk(prompt, history)

# ------------------------
# Random Game or Fun Choice
# ------------------------
def random_event(history=[]):
    event_type = random.choice(["mini_game", "fun_fact", "ai_talk", "countdown"])
    if event_type == "mini_game":
        play_mini_game()
    elif event_type == "fun_fact":
        random_fun_fact()
    elif event_type == "ai_talk":
        start_conversation(history)
    elif event_type == "countdown":
        countdown(random.randint(3,7))

# ------------------------
# Batch Fun Messages
# ------------------------
def batch_random_messages(n=5):
    for _ in range(n):
        random_message()
        time.sleep(random.uniform(0.3,0.8))

# ------------------------
# Test / Example Usage
# ------------------------
if __name__ == "__main__":
    print(WHITE + "=== Extras Module Test ===" + RESET)
    print(random_greeting())
    batch_random_messages(3)
    quick_fact("Python (programming language)")
    ai_small_talk("Explain black holes in simple terms")
    play_mini_game()
    random_event()
    print(random_farewell())
