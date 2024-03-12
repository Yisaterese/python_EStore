from tictactoe import tictactoe
from tictactoe.cellvalues import CellValues
from tictactoe.invalidBordCellException import InvalidBordCellException
from tictactoe.player import *
from tictactoe.tictactoe import TicTacToe

tictactoe = TicTacToe()


def execute_tictactoe_game():
    player_X = Player("X")
    player_O = Player("O")
    current_player = player_X

    if current_player == CellValues.X:
        return CellValues.X
    elif current_player == player_O:
        return CellValues.O


print("     GAME START")
while True:
    input_cell = int(input())
    try:
        tictactoe.validate_board_range(input_cell)
    except InvalidBordCellException as ex:
        tictactoe.validate_board_range(input_cell)
    else:



