import sys
import math
PIECES = {
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙",
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    ".": "·"
}

class ChessGame:
    def __init__(self):
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        self.turn = "White"

    def print_board(self):
        print("\n    a  b  c  d  e  f  g  h")
        print("  +------------------------+")
        for i, row in enumerate(self.board):
            row_str = f"{8 - i} |"
            for piece in row:
                row_str += f" {PIECES[piece]} "
            row_str += f"| {8 - i}"
            print(row_str)
        print("  +------------------------+")
        print("    a  b  c  d  e  f  g  h\n")

    def parse_coordinates(self, move_str):
        try:
            if len(move_str) != 4:
                return None
            start_col = ord(move_str[0].lower()) - ord('a')
            start_row = 8 - int(move_str[1])
            end_col = ord(move_str[2].lower()) - ord('a')
            end_row = 8 - int(move_str[3])
            
            if all(0 <= x < 8 for x in [start_row, start_col, end_row, end_col]):
                return start_row, start_col, end_row, end_col
        except ValueError:
            return None
        return None

    def check_move(self, move):
        coords = self.parse_coordinates(move)
        if not coords:
            return False
        sr, sc, er, ec = coords
        piece = self.board[sr][sc]
        dx = er - sr
        dy = ec - sc
        if piece == ".":
            return False
        else:
            if piece.lower() == "p":
                if self.turn == "White":
                    if sc == ec:
                        if dx == -1 and self.board[er][ec] == ".":
                            return True
                        elif dx == -2 and sr == 6 and self.board[er][ec] == ".":
                            return True
                    elif abs(sc - ec) == 1 and dx == -1:
                        if self.board[er][ec] != ".":
                            return True
                elif self.turn == "Black":
                    if sc == ec:
                        if dx == 1 and self.board[er][ec] == ".":
                            return True
                        elif dx == 2 and sr == 1 and self.board[er][ec] == ".":
                            return True
                    elif abs(sc - ec) == 1 and dx == 1:
                        if self.board[er][ec] != ".":
                            return True
                return False
            elif piece.lower() == "b":
                if abs(dx) == abs(dy) and dx != 0:
                    return True
                else:
                    return False 
            elif piece.lower() == "r":
                if (dx == 0 and dy != 0) or (dy == 0 and dx != 0):
                    return True
                else:
                    return False
            elif piece.lower() == "q":
                if (dx == 0 and dy != 0) or (dy == 0 and dx != 0) or (abs(dx) == abs(dy) and dx != 0):
                    return True
                else:
                    return False
            elif piece.lower() == "k":
                if abs(dx) <= 1 and abs(dy) <= 1 and not (dx == 0 and dy == 0):
                    return True 
                else:
                    return False
            elif piece.lower() == "n":
                if (abs(dx) == 1 and abs(dy) == 2) or (abs(dx) == 2 and abs(dy) == 1):
                    return True
                else:
                    return False
        return False

    def make_move(self, move_str):
        coords = self.parse_coordinates(move_str)
        if not coords:
            print("❌ Invalid syntax! Use format like 'e2e4'.")
            return False

        sr, sc, er, ec = coords
        print(coords)
        piece = self.board[sr][sc]

        if piece == ".":
            print("❌ There is no piece on the starting square!")
            return False

        if self.turn == "White" and not piece.isupper():
            print("❌ It is White's turn!")
            return False
        if self.turn == "Black" and not piece.islower():
            print("❌ It is Black's turn!")
            return False
        if not self.check_move(move_str):
            return False    
        target = self.board[er][ec]
        if target != "." and (piece.isupper() == target.isupper()):
            print("❌ You cannot capture your own piece!")
            return False

        self.board[er][ec] = piece
        self.board[sr][sc] = "."
        print(coords)
        self.turn = "Black" if self.turn == "White" else "White"
        return True

    def play(self):
        print("Welcome to Terminal Chess!")
        print("Enter moves using 4-character notation (e.g., e2e4, g1f3). Type 'exit' to quit.")
        
        while True:
            self.print_board()
            move = input(f"{self.turn} to move: ").strip()
            
            if move.lower() == 'exit':
                print("Thanks for playing!")
                break
            success = self.make_move(move)
            if not success:
                print("Please try your move again.")

if __name__ == "__main__":
    game = ChessGame()
    game.play()