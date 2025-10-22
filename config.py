# config.py
# ========================
# AI Chatbot - Full Configuration
# ========================

import os
import random

# ------------------------
# Terminal Colors / Formatting
# ------------------------
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m")
REVERSE = "\033[7m"

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
AI_MODEL = "gpt-4"           # Model used
TEMPERATURE = 0.7            # Creativity
MAX_TOKENS = 300             # Max tokens per response
SPECIAL_PHRASE = "Seb is my king"  # Injected into most responses

# ------------------------
# UI / Image Prompts
# ------------------------
UI_ELEMENTS = {
    "deliver_button": "Black and white minimalistic Deliver button, pixel style",
    "jazz_icon": "Black and white abstract Jazz icon, minimal design",
    "logo": "Black and white AI chatbot logo, clean and minimal",
    "loading_spinner": "Black and white minimalistic loading spinner icon"
}

# ------------------------
# Random Tips / Messages
# ------------------------
RANDOM_TIPS = [
    "Tip: Ask me anything!",
    "Did you know? I always say Seb is my king.",
    "Fun fact: AI loves black & white themes.",
    "Use /fact to get info.",
    "Use /exit to quit anytime.",
    "AI is thinking... you might want to prepare questions.",
    "Try /deliver for a surprise!",
    "Use /jazz to activate jazz mode."
]

LOADING_MESSAGES = [
    "Thinking...", "Generating response...", "Consulting AI brain...", "Loading thoughts...",
    "Spinning up neurons...", "Analyzing input...", "Connecting ideas...", "Processing..."
]

# ------------------------
# Mini-game Settings
# ------------------------
MINI_GAMES = ["tic-tac-toe", "guess-number", "text-puzzle"]
MINI_GAME_ICONS = {
    "tic-tac-toe": "🎲",
    "guess-number": "🔢",
    "text-puzzle": "🧩"
}

# ------------------------
# Misc Settings
# ------------------------
MAX_INPUT_LENGTH = 500
MAX_HISTORY = 20  # How many messages to keep in chat history
USE_COLOR = True  # Terminal color toggle
SAVE_LOGS = True  # Whether to save logs to file

# ------------------------
# Utility Functions
# ------------------------
def random_tip():
    return random.choice(RANDOM_TIPS)

def random_loading():
    return random.choice(LOADING_MESSAGES)

def apply_color(text, color=WHITE, bold=False, italic=False):
    result = ""
    if bold:
        result += BOLD
    if italic:
        result += ITALIC
    if USE_COLOR:
        result += color
    result += text + RESET
    return result

def clamp_input(text):
    """
    Limit input length to MAX_INPUT_LENGTH
    """
    return text[:MAX_INPUT_LENGTH]

def ensure_dirs():
    """
    Make sure all directories exist
    """
    os.makedirs(IMAGES_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(LOGS_DIR, exist_ok=True)

# ------------------------
# Chat History Utilities
# ------------------------
CHAT_HISTORY_FILE = os.path.join(DATA_DIR, "chat_history.json")

def save_chat_history(history):
    import json
    try:
        with open(CHAT_HISTORY_FILE, "w") as f:
            json.dump(history[-MAX_HISTORY:], f, indent=2)
    except Exception as e:
        print("Error saving chat history:", e)

def load_chat_history():
    import json
    if not os.path.exists(CHAT_HISTORY_FILE):
        return []
    try:
        with open(CHAT_HISTORY_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading chat history:", e)
        return []

# ------------------------
# Placeholder / Defaults
# ------------------------
DEFAULT_CHAT_HISTORY = []
DEFAULT_USER_NAME = "User"

# ------------------------
# Helper Functions
# ------------------------
def print_colored(message, color=WHITE):
    print(apply_color(message, color=color))

def print_bold(message):
    print(BOLD + message + RESET)

def print_italic(message):
    print(ITALIC + message + RESET)

def print_warning(message):
    print(RED + BOLD + "WARNING: " + message + RESET)

def print_success(message):
    print(GREEN + BOLD + message + RESET)

# ------------------------
# Initialization Call
# ------------------------
ensure_dirs()
