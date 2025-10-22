# utils.py
# ========================
# AI Chatbot - Utilities and Logging
# ========================

import os
import json
import time
import random
from config import *

# ------------------------
# File Paths
# ------------------------
CHAT_LOG_FILE = os.path.join(LOGS_DIR, "chat_log.txt")
SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")

# ------------------------
# Chat Logging Functions
# ------------------------
def log_message(user, message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if SAVE_LOGS:
        try:
            with open(CHAT_LOG_FILE, "a") as f:
                f.write(f"[{timestamp}] {user}: {message}\n")
        except Exception as e:
            print(RED + f"Error writing log: {e}" + RESET)

def load_chat_log():
    if not os.path.exists(CHAT_LOG_FILE):
        return []
    try:
        with open(CHAT_LOG_FILE, "r") as f:
            return f.readlines()
    except Exception as e:
        print(RED + f"Error loading log: {e}" + RESET)
        return []

def clear_chat_log():
    if os.path.exists(CHAT_LOG_FILE):
        os.remove(CHAT_LOG_FILE)
        print(GREEN + "Chat log cleared." + RESET)

# ------------------------
# Chat History Management
# ------------------------
def save_chat_history(history, filename=CHAT_HISTORY_FILE):
    try:
        with open(filename, "w") as f:
            json.dump(history[-MAX_HISTORY:], f, indent=2)
    except Exception as e:
        print(RED + f"Error saving chat history: {e}" + RESET)

def load_chat_history(filename=CHAT_HISTORY_FILE):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        print(RED + f"Error loading chat history: {e}" + RESET)
        return []

# ------------------------
# Settings Management
# ------------------------
def save_settings(settings):
    try:
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f, indent=2)
    except Exception as e:
        print(RED + f"Error saving settings: {e}" + RESET)

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {}
    try:
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(RED + f"Error loading settings: {e}" + RESET)
        return {}

# ------------------------
# Helper: Delays and Animations
# ------------------------
def loading_animation(message="Loading", seconds=1.5):
    for _ in range(int(seconds*4)):
        print(WHITE + message + "." * random.randint(1,3) + RESET, end="\r")
        time.sleep(0.25)
    print(" " * 50, end="\r")

def type_writer(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# ------------------------
# Tips and Fun Messages
# ------------------------
def random_tip():
    return random.choice(RANDOM_TIPS)

def random_fun_message():
    messages = [
        "Don't forget, Seb is my king!",
        "AI loves black & white themes.",
        "Try mini-games to pass the time.",
        "Use /fact to learn something new.",
        "Keep chatting with AI for fun!"
    ]
    return random.choice(messages)

# ------------------------
# Helper: Clear Screen
# ------------------------
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

# ------------------------
# Test / Example Usage
# ------------------------
if __name__ == "__main__":
    print(WHITE + "=== Utils Module Test ===" + RESET)
    log_message("TestUser", "This is a test message.")
    history = [{"role": "user", "content": "Hello"}, {"role": "ai", "content": "Hi!"}]
    save_chat_history(history)
    loaded = load_chat_history()
    print("Loaded History:", loaded)
    save_settings({"theme":"black_white","volume":7})
    print("Settings:", load_settings())
    type_writer("Testing typewriter effect...")
    loading_animation("Testing animation",2)
    print(random_tip())
    print(random_fun_message())
    clear_screen()
    print(GREEN + "Utils module test complete." + RESET)
