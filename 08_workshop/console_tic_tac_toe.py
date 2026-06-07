def show_board(game_board):
    for r in game_board:
        print(f"| {' | '.join(r)} |")


def row_winner(game_board, sym):
    for r in game_board:
        if r.count(sym) == 3:
            return True
    return None


def col_winner(game_board, sym):
    matching_symbols = 0
    for c in range(3):
        matching_symbols = 0
        for r in range(3):
            if board[r][c] == sym:
                matching_symbols += 1

        if matching_symbols == 3:
            return True
    return None


def diag_winner(game_board, sym):
    primary_d_matching_symbols = 0
    secondary_d_matching_symbols = 0
    for r in range(3):
        if board[r][r] == sym:
            primary_d_matching_symbols += 1
        if board[r][3 - r - 1] == sym:
            secondary_d_matching_symbols += 1

    if primary_d_matching_symbols == 3 or secondary_d_matching_symbols == 3:
        return True
    return None


def check_for_winner(game_board, sym):
    if row_winner(game_board, sym) or col_winner(game_board, sym) or diag_winner(game_board, sym):
        return True
    return False


first_player = input("Player one name: ")
second_player = input("Player two name: ")
symbol_of_first_player = input(f"{first_player} would you like play with 'X' or 'O'? -> ").upper()

while symbol_of_first_player not in ["X", "O"]:
    print("Please enter a valid symbol!")
    symbol_of_first_player = input(f"{first_player} would you like play with 'X' or 'O'? -> ").upper()

symbol_of_second_player = "O" if symbol_of_first_player == "X" else "X"

turn = 1
board = [[" ", " ", " "] for _ in range(3)]

positions = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

print()
print(f"{first_player} plays with: {symbol_of_first_player}")
print(f"{second_player} plays with: {symbol_of_second_player}\n")
print("This is the numeration of the board:")
print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")
print(f"{first_player} starts first!")

while turn < 10:
    current_symbol = symbol_of_first_player if turn % 2 != 0 else symbol_of_second_player
    current_player = first_player if turn % 2 != 0 else second_player

    #Checking if the input is valid or a valid number
    try:
        move = int(input(f"{current_player} choose a free position [1-9]: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if not (1 <= move <= 9):
        print("Please enter a valid number, between 1 and 9!")
        continue

    row, col = positions[move]

    #Checking if the input is a free position
    if board[row][col] == " ":
        board[row][col] = current_symbol
        show_board(board)
    else:
        print("Please choose a free position!")
        continue

    #Checking for winner
    if turn >= 5:
        if check_for_winner(board, current_symbol):
            print(f"WE HAVE A WINNER!\n{current_player} wins!")
            break

    turn += 1

else:
    print("We don't have a winner!")