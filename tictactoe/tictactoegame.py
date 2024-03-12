from tictactoe import tictactoe
from tictactoe.invalidBordCellException import InvalidBordCellException
from tictactoe.player import *
from tictactoe.tictactoe import TicTacToe

tictactoe = TicTacToe()
player_X = Player("X")
player_O = Player("O")
current_player = player_X


def player_turn(current_player):

    if current_player == CellValues.X:
        return CellValues.X
    elif current_player == player_O:
        return CellValues.O


def execute_tictactoe_game(input_cell):
    try:
        tictactoe.validate_board_range(input_cell)
    except InvalidBordCellException as ex:
        tictactoe.validate_board_range(input_cell)
    else:
        print("     GAME START")
        while True:

            current_player.make_move(input_cell, CellValues.value)
            current_player.display_board_cells()
            print("player" + current_player.getName() + "make move")
            if tictactoe.winner:
                break
            else:
                return tictactoe.draw_game()


print("player" + current_player.getName() + "won")
