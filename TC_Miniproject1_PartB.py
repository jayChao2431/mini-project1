from enum import Enum, auto
from typing import List, Tuple

# Game constants
COL_SIZE = 7
ROW_SIZE = 6


class Cell(Enum):
    X = auto()
    O = auto()
    EMPTY = auto()


class Player(Enum):
    X = auto()
    O = auto()

    def next_player(self) -> "Player":
        """Return the next player."""
        return Player.O if self == Player.X else Player.X


def create_empty_board() -> List[List[Cell]]:
    """Create an empty game board."""
    return [[Cell.EMPTY for _ in range(COL_SIZE)] for _ in range(ROW_SIZE)]


def is_winner(
    board: List[List[Cell]], player: Player, row: int, col: int
) -> bool:
    """Check if the player has won after their move."""
    def check_diagonal_line(cell,row,col,row_offset,col_offset):
        """Check the cells of diagonal line is all the same."""
        diagonal_index = ((row + row_offset*i,col + col_offset*i) for i in range(1,4))
        try:
            return all(board[r][c] == cell for r,c in diagonal_index)
        except IndexError:
            return False
    cell: Cell = getattr(Cell, player.name)
    try:
        # Check left-side
        if all(board[row][c] == cell for c in range(col - 3, col)):
            return True

        # Check right-side
        if all(board[row][c] == cell for c in range(col + 1, col + 4)):
            return True

        # Check top-side
        if all(board[r][col] == cell for r in range(row + 1, row + 4)):
            return True

        # Check bottom-side
        if all(board[r][col] == cell for r in range(row - 3, row)):
            return True
    except IndexError:
        return False

    # Check diagonal line
    directions = ((1,1),(-1,1),(-1,-1),(-1,1))
    if any(check_diagonal_line(cell,row,col,row_offset,col_offset) for row_offset,col_offset in directions):
        return True
    return False

def print_board(board: List[List[Cell]]) -> None:
    """Print the game board"""
    footer : str = (
        "|R\\C|" + " |".join(f" {chr(ord("a") + i)}" for i in range(COL_SIZE)) + " |"
    )
    separator: str = "-" * len(footer)
    for row in reversed(range(ROW_SIZE)):
        row_str: str = f"| {row+1} |" # Because we use zero-based row
        for col in range(COL_SIZE):
            if board[row][col] == Cell.X:
                row_str += " X |"
            elif board[row][col] == Cell.O:
                row_str += " O |"
            else:
                row_str += "   |"
        print(row_str)
        print(separator)
    print(footer)
    print()  # Make sure there is a newline

def get_available_positions(board: List[List[Cell]]) -> List[str]:
    """Return available positions"""
    l = []
    for col_index in range(COL_SIZE):
        for row_index in range(ROW_SIZE):
            if board[row_index][col_index] == Cell.EMPTY:
                l.append(f"{chr(ord("a")+col_index)}{row_index+1}")
                break
    return l
        


def get_player_move(
    board: List[List[Cell]], player: Player
) -> Tuple[int, int]:
    """Get and validate the player's move then put into board."""
    while True:
        print(f"{player.name}'s turn.")
        print(f"Where do you want your {player.name} placed?")
        available_pos = get_available_positions(board)
        print(f"Available positions are: {available_pos}\n")
        user_input = input("Please enter column-letter and row-number (e.g., a1): ")
        if user_input not in available_pos:
            print(f"Invalid entry: try again.\n{user_input} is not available.")
            continue
        col,row = user_input
        col = ord(col) - ord("a")
        row = int(row) - 1 # Because we use zero-based row
        board[row][col] = getattr(Cell, player.name)
        return row,col

def play_game() -> None:
    """Play a single game of Connect Four"""
    board = create_empty_board()
    current_player = Player.X
    print(f"\nNew Game: {current_player.name} goes first.\n")
    remain_steps = ROW_SIZE * COL_SIZE    
    while remain_steps > 0:
        row, col = get_player_move(board, current_player)
        print("Thank you for your selection.")
        print_board(board)

        if is_winner(board, current_player, row, col):
            print(f"{current_player.name} IS THE WINNER!!!")
            return
        current_player = current_player.next_player()
        remain_steps -= 1
    print("DRAW! NOBODY WINS!")

def main() -> None:
    """Main game loop"""
    while True:
        play_game()
        user_input: str = input("Another game (y/n)? ")
        if user_input != "y":
            break
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
