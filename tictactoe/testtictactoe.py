from tictactoe.tictactoe import TicTacToe


def test_the_number_of_cell_in_board_cells():
    tictactoe = TicTacToe()
    tictactoe.populate_board_cells()
    assert tictactoe.get_number_of_cells() == 3