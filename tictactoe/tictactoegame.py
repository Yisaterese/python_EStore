from tictactoe.cellvalues import CellValues
from tictactoe.player import Player
from tictactoe.tictactoe import TicTacToe


def execute_tictactogame():
    player_X = Player("X")
    player_O = Player("O")
    current_player = player_X

    if current_player == CellValues.X:
        return CellValues.X
    elif current_player == player_O:
        return CellValues.O
