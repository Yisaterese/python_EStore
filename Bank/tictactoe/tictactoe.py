from Bank.tictactoe.cellvalues import CellValues


class TicTacToe:
    def __init__(self):
        self.board_cells = [[], [], []]

    def populate_board_cells(self):
        for row in range(0,3):
            for col in range(0, 3):
                self.board_cells[row][col] = CellValues.EMPTY

    def get_number_of_cells(self) -> int:
        return len(self.board_cells)
