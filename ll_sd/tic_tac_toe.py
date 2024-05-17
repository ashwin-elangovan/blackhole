from abc import ABC, abstractmethod
from random import choice

# Abstract class for Players
class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board):
        pass

# Concrete class for Human Players
class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            move = input(f"Your move (1-9): ")
            if move in board.available_moves():
                return int(move)
            print("Invalid move. Try again.")

# Concrete class for Computer Players
class ComputerPlayer(Player):
    def get_move(self, board):
        return choice(board.available_moves())

# Class for representing the Board
class Board:
    def __init__(self):
        self.cells = [None] * 9

    def available_moves(self):
        return [i + 1 for i, cell in enumerate(self.cells) if cell is None]

    def make_move(self, move, player):
        self.cells[move - 1] = player.symbol

    def is_win(self, player):
        for i in range(3):
            if all(self.cells[i * 3 + j] == player.symbol for j in range(3)):
                return True  # Horizontal win
            if all(self.cells[i + j * 3] == player.symbol for j in range(3)):
                return True  # Vertical win

        if all(self.cells[i] == player.symbol for i in [0, 4, 8]):
            return True  # Diagonal win
        if all(self.cells[i] == player.symbol for i in [2, 4, 6]):
            return True  # Diagonal win

        return False

    def is_tie(self):
        return all(cell is not None for cell in self.cells)

    def display(self):
        for i in range(3):
            print("|".join(self.cells[i * 3:i * 3 + 3]))
            if i < 2:
                print("-+-+-")

# Game class
class TicTacToeGame:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    def play(self):
        current_player = self.player1

        while True:
            self.board.display()
            move = current_player.get_move(self.board)
            self.board.make_move(move, current_player)

            if self.board.is_win(current_player):
                self.board.display()
                print(f"{current_player.symbol} wins!")
                break

            if self.board.is_tie():
                self.board.display()
                print("Tie game!")
                break

            current_player = self.player2 if current_player == self.player1 else self.player1

# Usage
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    player1_symbol = input("Choose your symbol (X/O): ")
    player1 = HumanPlayer(player1_symbol)
    player2 = ComputerPlayer("X" if player1_symbol == "O" else "O")

    game = TicTacToeGame(player1, player2)
    game.play()
