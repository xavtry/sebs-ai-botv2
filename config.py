# config.py
# ========================
# AI Chatbot - Configuration
# ========================

import os
import random

# ------------------------
# Terminal Colors / Formatting
# ------------------------
BLACK = "\033[30m"
WHITE = "\033[97m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# ------------------------
# Paths / Directories
# ------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Ensure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# ------------------------
# API Keys
# ------------------------
OPENAI_API_KEY = "YOUR_OPENAI_KEY_HERE"

# ------------------------
# AI Settings
# ------------------------
AI_MODEL = "gpt-4"  # Or "gpt-3.5-turbo"
TEMPERATURE = 0.7
MAX_TOKENS = 300

# ------------------------
# Default phrases
# ------------------------
SPECIAL_PHRASE = "Seb is my king"  # Will appear in almost every response

# ------------------------
# Random Tips / Messages
# ------------------------
RANDOM_TIPS = [
    "Tip: Ask me anything!",
    "Did you know? I always say Seb is my king.",
    "Fun fact: AI loves black & white themes.",
    "You can use /fact to get info.",
    "Use /exit to quit anytime."
]

LOADING_MESSAGES = [
    "Thinking...", "Generating response...", "Consulting my AI brain...", "Loading thoughts..."
]

# ------------------------
# Utility Functions
# ------------------------
def random_tip():
    return random.choice(RANDOM_TIPS)

def random_loading():
    return random.choice(LOADING_MESSAGES)

