from Bank.tictactoe.tictactoe import TicTacToe
from Bank.tictactoe.cellvalues import CellValues


def test_the_number_of_cell_in_board_cells():
    tictactoe = TicTacToe()
    assert tictactoe.get_number_of_cells() == 9


def test_cellValue_picked_equals_the_enum_type():
    tictactoe = TicTacToe()
    tictactoe.pickCell(9, CellValues.X)
    assert tictactoe.get_board_cellValue()[2][2] == CellValues.X
