
# features.py
# ========================
# AI Chatbot - Mini-Games and Extra Features
# ========================

import random
import time
from config import *

# ------------------------
# Tic-Tac-Toe Game
# ------------------------
def print_board(board):
    print(WHITE)
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print(RESET)

def check_winner(board, symbol):
    # Rows, Columns, Diagonals
    for i in range(3):
        if all([board[i][j] == symbol for j in range(3)]):
            return True
        if all([board[j][i] == symbol for j in range(3)]):
            return True
    if all([board[i][i] == symbol for i in range(3)]):
        return True
    if all([board[i][2-i] == symbol for i in range(3)]):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    ai = "O"
    print(WHITE + "Welcome to Tic-Tac-Toe!" + RESET)
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            # Player move
            while True:
                try:
                    move = input("Enter your move (row,col 0-2): ")
                    r, c = map(int, move.split(","))
                    if board[r][c] == " ":
                        board[r][c] = player
                        break
                    else:
                        print("Cell occupied!")
                except:
                    print("Invalid input. Use row,col (0-2)")
        else:
            # AI move
            empty = [(i,j) for i in range(3) for j in range(3) if board[i][j]==" "]
            r,c = random.choice(empty)
            board[r][c] = ai

        print_board(board)

        if check_winner(board, player):
            print(GREEN + "You win!" + RESET)
            return
        if check_winner(board, ai):
            print(RED + "AI wins!" + RESET)
            return
    print(YELLOW + "It's a tie!" + RESET)

# ------------------------
# Guess-the-Number Game
# ------------------------
def guess_number():
    number = random.randint(1, 100)
    print(WHITE + "Guess the number between 1 and 100!" + RESET)
    attempts = 0
    while True:
        guess = input("Your guess: ")
        attempts +=1
        try:
            guess = int(guess)
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(GREEN + f"Correct! The number was {number}. Attempts: {attempts}" + RESET)
                break
        except:
            print("Enter a valid number.")

# ------------------------
# Text Puzzle Game
# ------------------------
def text_puzzle():
    puzzles = [
        {"q": "I speak without a mouth and hear without ears. What am I?", "a": "echo"},
        {"q": "I’m tall when I’m young, and I’m short when I’m old. What am I?", "a": "candle"},
        {"q": "What has keys but can't open locks?", "a": "piano"},
        {"q": "I have cities, but no houses. What am I?", "a": "map"},
    ]
    puzzle = random.choice(puzzles)
    print(WHITE + "Text Puzzle:" + RESET)
    print(puzzle["q"])
    answer = input("Answer: ").strip().lower()
    if answer == puzzle["a"]:
        print(GREEN + "Correct!" + RESET)
    else:
        print(RED + f"Wrong! The answer was {puzzle['a']}." + RESET)

# ------------------------
# Mini-Game Selector
# ------------------------
def mini_game_menu():
    print(WHITE + "Mini-Games Available:" + RESET)
    for i, game in enumerate(MINI_GAMES):
        print(f"{i+1}. {game} {MINI_GAME_ICONS.get(game,'')}")
    choice = input("Select a game by number: ")
    try:
        choice = int(choice)
        if choice == 1:
            tic_tac_toe()
        elif choice == 2:
            guess_number()
        elif choice == 3:
            text_puzzle()
        else:
            print("Invalid selection.")
    except:
        print("Invalid input.")

# ------------------------
# Extra Fun Feature
# ------------------------
def random_fun_fact():
    facts = [
        "Did you know? Honey never spoils.",
        "Did you know? A group of flamingos is called a flamboyance.",
        "Did you know? Octopuses have three hearts.",
        "Fun fact: I always say Seb is my king."
    ]
    print(WHITE + random.choice(facts) + RESET)

# ------------------------
# Test / Example Usage
# ------------------------
if __name__ == "__main__":
    print(WHITE + "=== Mini-Games Test ===" + RESET)
    while True:
        print("\nOptions:")
        print("1. Tic-Tac-Toe")
        print("2. Guess-the-Number")
        print("3. Text Puzzle")
        print("4. Random Fun Fact")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            tic_tac_toe()
        elif choice == "2":
            guess_number()
        elif choice == "3":
            text_puzzle()
        elif choice == "4":
            random_fun_fact()
        elif choice == "5":
            print(WHITE + "Exiting Mini-Games." + RESET)
            break
        else:
            print("Invalid choice.")
