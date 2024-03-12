from tictactoe.cellvalues import CellValues
from tictactoe.tictactoe import TicTacToe


class Player:
    def __init__(self, name):
        self.name = name

    def make_move(self, input: int, cell_value: CellValues):
        tictactoe = TicTacToe()
        tictactoe.pickCell(input, cell_value)
