import random

board = [" "] * 9

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner():
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None

def computer_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"

print("TIC-TAC-TOE")
print("You are X. Computer is O.")
print("Choose positions from 1 to 9.")

while True:
    print_board()

    
    try:
        move = int(input("Enter your move (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Please enter a number between 1 and 9.")
            continue

        if board[move] != " ":
            print("That position is already taken.")
            continue

        board[move] = "X"

    except ValueError:
        print("Please enter a valid number.")
        continue

    result = check_winner()

    if result:
        print_board()
        if result == "Draw":
            print("It's a draw!")
        else:
            print(f"{result} wins!")
        break

    computer_move()
    print("Computer has made its move.")

    result = check_winner()

    if result:
        print_board()
        if result == "Draw":
            print("It's a draw!")
        else:
            print(f"{result} wins!")
        break
