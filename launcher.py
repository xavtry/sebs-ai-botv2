# launcher.py
# ========================
# AI Chatbot - Launcher / Integration
# ========================

import time
from config import *
from main import chat_loop
from features import mini_game_menu
from extras import random_greeting, random_message, random_event

# ------------------------
# Loading Animation
# ------------------------
def loading_animation(message="Loading", seconds=1.5):
    for _ in range(int(seconds*4)):
        print(WHITE + message + "." * random.randint(1,3) + RESET, end="\r")
        time.sleep(0.25)
    print(" " * 50, end="\r")

# ------------------------
# Main Menu Display
# ------------------------
def print_main_menu():
    print(BOLD + WHITE + "\n=== AI Chatbot Launcher ===\n" + RESET)
    print("1. Start Chat")
    print("2. Play Mini-Game")
    print("3. Extras / Fun Features")
    print("4. Exit")
    print()

# ------------------------
# Extras Menu
# ------------------------
def extras_menu():
    print(WHITE + "\nExtras Menu:" + RESET)
    print("1. Random Greeting")
    print("2. Random Fun Message")
    print("3. Random Event")
    print("4. Back to Main Menu")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        print(random_greeting())
    elif choice == "2":
        random_message()
    elif choice == "3":
        random_event()
    elif choice == "4":
        return
    else:
        print(WHITE + "Invalid selection." + RESET)

# ------------------------
# Main Launcher Loop
# ------------------------
def launcher_loop():
    while True:
        print_main_menu()
        choice = input("Select an option: ").strip()
        if choice == "1":
            loading_animation("Launching Chat")
            chat_loop()
        elif choice == "2":
            loading_animation("Launching Mini-Game")
            mini_game_menu()
        elif choice == "3":
            extras_menu()
        elif choice == "4":
            print(WHITE + "Exiting. Goodbye!" + RESET)
            break
        else:
            print(WHITE + "Invalid choice, try again." + RESET)
        time.sleep(0.5)

# ------------------------
# Main
# ------------------------
if __name__ == "__main__":
    loading_animation("Starting AI Chatbot Launcher", 2)
    launcher_loop()
