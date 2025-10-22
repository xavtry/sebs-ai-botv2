# main.py
# ========================
# AI Chatbot - Main Entry
# ========================

import os
import time
import random
from config import *
from ai_responses import get_ai_response
from fact_lookup import get_fact
from ui_generator import generate_ui_image

# ------------------------
# Logging
# ------------------------
LOG_FILE = os.path.join(LOGS_DIR, "chat_log.txt")

def log_message(user, message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {user}: {message}\n")

# ------------------------
# Loading Animation
# ------------------------
def loading_animation(seconds=1.5):
    msg = random_loading()
    for _ in range(int(seconds * 4)):
        print(WHITE + msg + "." * random.randint(1, 3) + RESET, end="\r")
        time.sleep(0.25)
    print(" " * 50, end="\r")

# ------------------------
# Intro / ASCII Logo
# ------------------------
def print_intro():
    logo_path = os.path.join(IMAGES_DIR, "logo.png")
    print(BOLD + WHITE + "\n=== AI CHATBOT ===\n" + RESET)
    if os.path.exists(logo_path):
        print(f"[Logo loaded from {logo_path}]")
    else:
        print("[Logo not found. Generating AI logo...]")
        loading_animation(2)
        generate_ui_image("Black and white minimalistic AI logo", "logo.png")
        print("[Logo generated!]\n")
    print(random_tip())
    print("\nType /help for commands.\n")

# ------------------------
# Command Handling
# ------------------------
def handle_command(command):
    command = command.strip()
    log_message("USER", command)

    if command.startswith("/fact"):
        topic = command[6:].strip()
        if not topic:
            print(WHITE + "Please provide a topic for /fact." + RESET)
            return
        loading_animation()
        fact = get_fact(topic)
        print(WHITE + f"[FACT] {fact}" + RESET)

    elif command.startswith("/deliver"):
        print(WHITE + "[Deliver button pressed!]" + RESET)
        img_path = os.path.join(IMAGES_DIR, "deliver_button.png")
        if not os.path.exists(img_path):
            loading_animation()
            generate_ui_image("Black and white Deliver button", "deliver_button.png")
        print(f"[Button image at {img_path}]")

    elif command.startswith("/jazz"):
        print(WHITE + "[Jazz mode activated!]" + RESET)
        img_path = os.path.join(IMAGES_DIR, "jazz_icon.png")
        if not os.path.exists(img_path):
            loading_animation()
            generate_ui_image("Black and white Jazz icon", "jazz_icon.png")
        print(f"[Jazz icon at {img_path}]")

    elif command == "/help":
        print(WHITE + """
Available Commands:
/fact <topic>        - Get factual info
/deliver             - Press deliver button
/jazz                - Activate jazz mode
/exit                - Quit chatbot
""" + RESET)

    else:
        # Default: AI-generated response
        loading_animation()
        ai_text = get_ai_response(command)
        print(WHITE + ai_text + RESET)

# ------------------------
# Chat Loop
# ------------------------
def chat_loop():
    print_intro()
    while True:
        user_input = input(BOLD + WHITE + "You> " + RESET)
        if user_input.lower() in ["/exit", "quit"]:
            print(WHITE + "Goodbye!" + RESET)
            break
        handle_command(user_input)
        time.sleep(0.2)
        print(random_tip())

# ------------------------
# Main
# ------------------------
if __name__ == "__main__":
    chat_loop()

