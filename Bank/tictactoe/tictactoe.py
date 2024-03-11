from Bank.tictactoe.cellvalues import CellValues
from Bank.tictactoe.invalidBordCellException import InvalidBordCellException


class TicTacToe:
    def __init__(self):
        self.board_cells = [[CellValues.EMPTY, CellValues.EMPTY, CellValues.EMPTY],
                            [CellValues.EMPTY, CellValues.EMPTY, CellValues.EMPTY],
                            [CellValues.EMPTY, CellValues.EMPTY, CellValues.EMPTY]]

    def populate_board_cells(self):
        for row in range(0, 3):
            for col in range(0, 3):
                self.board_cells[row][col] = CellValues.EMPTY

    def get_number_of_cells(self) -> int:
        return len(self.board_cells) * 3

    def pickCell(self, selectCell: int, cell_values: CellValues):
        self.validate_emptycell_onboard(selectCell, cell_values)
        self.validate_board_range(self, selectCell)

    def validate_emptycell_onboard(self, input_cell: int, cell_values: CellValues):
        row = (input_cell - 1) // 3
        col = (input_cell - 1) % 3
        if self.board_cells[row][col] == CellValues.EMPTY:
            self.board_cells[row][col] = cell_values
        else:
            raise InvalidBordCellException("Board cell is already picked")

    @staticmethod
    def validate_board_range(self, input_cell: int):
        if input_cell < 1 or input_cell > 9:
            raise InvalidBordCellException("Board cell out of range")

    def get_board_cellValue(self):
        return self.board_cells


tic = TicTacToe()
print(tic.get_number_of_cells())
