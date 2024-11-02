# Game constants
BOARD_SIZE = 3

# Constants for cell states
CELL_X = 'X'
CELL_O = 'O'
CELL_EMPTY = ' '

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'

def next_player(player):
    """Return the next player"""
    return PLAYER_O if player == PLAYER_X else PLAYER_X

def create_empty_board():
    """Create an empty game board"""
    return [[CELL_EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def is_winner(board, player, row, col):
    """Check if the player has won after their move"""
    # Check row
    if all(board[row][c] == player for c in range(BOARD_SIZE)):
        return True

    # Check column
    if all(board[r][col] == player for r in range(BOARD_SIZE)):
        return True

    # Check main diagonal
    if row == col and all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True

    # Check anti-diagonal
    if row + col == BOARD_SIZE - 1 and all(
        board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)
    ):
        return True
    return False

def print_board(board):
    """Print the game board"""
    header = "|R\\C|" + " |".join(f" {i}" for i in range(BOARD_SIZE)) + " |"
    separator = "-" * len(header)

    print(separator)
    print(header)
    print(separator)

    for row in range(BOARD_SIZE):
        row_str = f"| {row} |"
        for col in range(BOARD_SIZE):
            row_str += f" {board[row][col]} |"
        print(row_str)
        print(separator)
    print()  

def get_player_move(board, player):
    """Get and validate the player's move"""
    while True:
        print(f"{player}'s turn.")
        print(f"Where do you want your {player} placed?")
        try:
            row, col = map(
                int,
                input(
                    "Please enter row number and column number separated by a comma.\n"
                ).split(","),
            )
            print(f"You have entered row #{row}")
            print(f"          and column #{col}")

            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                if board[row][col] != CELL_EMPTY:
                    print(
                        "That cell is already taken.\n"
                        "Please make another selection.\n"
                    )
                    continue
                board[row][col] = player
                return row, col
            else:
                print(
                    "Invalid entry: try again.\nRow & column numbers must be either 0, 1, or 2.\n"
                )
        except ValueError:
            print("Invalid entry: try again.\n")

def play_game():
    """Play a single game of Tic-Tac-Toe"""
    board = create_empty_board()
    current_player = PLAYER_X
    print(f"\nNew Game: {current_player} goes first.\n")

    while True:
        row, col = get_player_move(board, current_player)
        print("Thank you for your selection.")
        print_board(board)

        if is_winner(board, current_player, row, col):
            print(f"{current_player} IS THE WINNER!!!")
            return

        if all(cell != CELL_EMPTY for row in board for cell in row):
            print("DRAW! NOBODY WINS!")
            return

        current_player = next_player(current_player)

def main():
    """Main game loop"""
    while True:
        play_game()
        user_input = input("Another game? Enter Y or y for yes.\n")
        if user_input.lower()[0] != "y":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
