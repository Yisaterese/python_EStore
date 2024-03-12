import pytest
from Bank.tictactoe.invalidBordCellException import InvalidBordCellException
from Bank.tictactoe.tictactoe import TicTacToe
from Bank.tictactoe.cellvalues import CellValues


def test_the_number_of_cell_in_board_cells():
    tictactoe = TicTacToe()
    assert tictactoe.get_number_of_cells() == 9


def test_cellValue_picked_equals_the_enum_type():
    tictactoe = TicTacToe()
    tictactoe.pickCell(9, CellValues.X)
    assert tictactoe.get_board_cellValue()[2][2] == CellValues.X


def test_cellValue_picked_equals_is_out_of_raise_exception():
    tictactoe = TicTacToe()
    with pytest.raises(InvalidBordCellException) as info:
        tictactoe.pickCell(10, CellValues.X)
        assert tictactoe.get_board_cellValue()[2][2] == CellValues.X
    assert str(info.value) == "Board cell out of range"


def test_win_by_row_get_win():
    tictactoe = TicTacToe()
    tictactoe.pickCell(1, CellValues.X)
    tictactoe.pickCell(4, CellValues.O)
    tictactoe.pickCell(2, CellValues.X)
    tictactoe.pickCell(5, CellValues.O)
    tictactoe.pickCell(3, CellValues.X)
    assert tictactoe.get_win_by_row() == CellValues.X


def test_win_by_column_get_win():
    tictactoe = TicTacToe()
    tictactoe.pickCell(1, CellValues.X)
    tictactoe.pickCell(2, CellValues.O)
    tictactoe.pickCell(4, CellValues.X)
    tictactoe.pickCell(5, CellValues.O)
    tictactoe.pickCell(9, CellValues.X)
    tictactoe.pickCell(8, CellValues.O)
    assert tictactoe.get_win_by_column() == CellValues.O


def test_win_by_diagonal_get_win():
    tictactoe = TicTacToe()
    tictactoe.pickCell(1, CellValues.X)
    tictactoe.pickCell(3, CellValues.O)
    tictactoe.pickCell(4, CellValues.X)
    tictactoe.pickCell(5, CellValues.O)
    tictactoe.pickCell(9, CellValues.X)
    tictactoe.pickCell(7, CellValues.O)
    assert tictactoe.get_win_by_diagonal() == CellValues.O


def test_for_winner():
    tictactoe = TicTacToe()
    tictactoe.pickCell(1, CellValues.X)
    tictactoe.pickCell(3, CellValues.O)
    tictactoe.pickCell(4, CellValues.X)
    tictactoe.pickCell(5, CellValues.O)
    tictactoe.pickCell(9, CellValues.X)
    tictactoe.pickCell(7, CellValues.O)
    assert tictactoe.get_winner() == CellValues.O


def test_for_draw_game():
    tictactoe = TicTacToe()
    tictactoe.pickCell(1, CellValues.X)
    tictactoe.pickCell(3, CellValues.O)
    tictactoe.pickCell(5, CellValues.X)
    tictactoe.pickCell(6, CellValues.O)
    tictactoe.pickCell(9, CellValues.X)
    tictactoe.pickCell(7, CellValues.O)
    tictactoe.pickCell(8, CellValues.X)
    tictactoe.pickCell(2, CellValues.O)
    tictactoe.pickCell(4, CellValues.X)

    assert tictactoe.draw_game() == tictactoe.get_board_cellValue()

