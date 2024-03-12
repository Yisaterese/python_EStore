from tictactoe.cellvalues import CellValues
from tictactoe.invalidBordCellException import InvalidBordCellException


class TicTacToe:
    def __init__(self):
        self.winner = None
        self.board_cells = [[CellValues.EMPTY, CellValues.EMPTY, CellValues.EMPTY],
                            [CellValues.EMPTY, CellValues.EMPTY, CellValues.EMPTY],
                            [CellValues.EMPTY, CellValues.EMPTY, CellValues.EMPTY]]

    def get_number_of_cells(self) -> int:
        return len(self.board_cells) * 3

    def pickCell(self, selectCell: int, cell_values: CellValues):
        self.validate_empty_cell_onboard(selectCell, cell_values)

    def validate_empty_cell_onboard(self, input_cell: int, cell_values: CellValues):
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

    def get_win_by_row(self):

        is_win_by_first_row = self.board_cells[0][0] == self.board_cells[0][1] and self.board_cells[0][1] == \
                              self.board_cells[0][2]
        is_win_by_second_row = self.board_cells[1][0] == self.board_cells[1][1] and self.board_cells[1][1] == \
                               self.board_cells[1][2]
        is_win_by_third_row = self.board_cells[2][0] == self.board_cells[2][1] and self.board_cells[2][1] == \
                              self.board_cells[2][2]
        if is_win_by_first_row:
            return self.board_cells[0][0]

        elif is_win_by_second_row:
            return self.board_cells[1][0]

        elif is_win_by_third_row:
            return self.board_cells[2][0]

    def get_win_by_column(self):

        is_won_by_first_column = self.board_cells[0][0] == self.board_cells[1][0] and self.board_cells[1][0] == \
                                 self.board_cells[2][0]
        is_won_by_second_column = self.board_cells[0][1] == self.board_cells[1][1] and self.board_cells[1][1] == \
                                  self.board_cells[2][1]
        is_won_by_third_column = self.board_cells[0][2] == self.board_cells[1][2] and self.board_cells[1][2] == \
                                 self.board_cells[2][2]
        if is_won_by_first_column:
            return self.board_cells[0][0]
        if is_won_by_second_column:
            return self.board_cells[0][1]
        if is_won_by_third_column:
            return self.board_cells[0][2]


    def get_win_by_diagonal(self):
        is_win_right__diagonal = self.board_cells[0][2] == self.board_cells[1][1] and self.board_cells[1][1] == \
                                 self.board_cells[2][0]
        is_win_by_left_diagonal = self.board_cells[0][0] == self.board_cells[1][1] and self.board_cells[1][1] == \
                                  self.board_cells[2][2]
        if is_win_right__diagonal or is_win_by_left_diagonal:
            return self.board_cells[1][1]

    def get_winner(self):

        if self.get_win_by_row():
            return self.get_win_by_row()
        if self.get_win_by_column():
            return self.get_win_by_column()
        if self.get_win_by_diagonal():
            return self.get_win_by_diagonal()

    def draw_game(self):
        if not self.get_win_by_row() or self.get_win_by_column() or self.get_win_by_diagonal():
            return self.get_board_cellValue()
