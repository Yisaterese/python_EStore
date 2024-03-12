from tictactoe.cellvalues import CellValues
from tictactoe.tictactoe import TicTacToe


class Player:
    tictactoe = TicTacToe()

    def __init__(self, name):
        self.name = name

    def make_move(self, input_cell: int, cell_value: CellValues):
        self.tictactoe.pickCell(input_cell, cell_value)

    def display_board_cells(self):
        print("_________________________")
        for row in range(len(self.tictactoe.board_cells)):
            print("|")
            for col in self.tictactoe.board_cells:
                print(self.tictactoe.board_cells[row][col])
            print()
            print("___________________________")

    def getName(self):
        return self.name
