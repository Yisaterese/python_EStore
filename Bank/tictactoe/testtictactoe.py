from Bank.tictactoe.tictactoe import TicTacToe
from Bank.tictactoe.cellvalues import CellValues


def test_the_number_of_cell_in_board_cells():
    tictactoe = TicTacToe()
    assert tictactoe.get_number_of_cells() == 9


def test_cellValue_picked_equals_the_enum_type():
    tictactoe = TicTacToe()
    print(tictactoe.get_number_of_cells())
    assert tictactoe.pickCell(3, CellValues.X) is CellValues.X



