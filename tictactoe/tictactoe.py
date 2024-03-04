class TicTacToe:
    def __init__(self):
        self.board_cells = [[]]

    def populate_board_cells(self):
        for row in range(0,3):
            for col in self.board_cells:
                self.board_cells = [row][col]

    def get_number_of_cells(self)-> int:
        return len(self.board_cells)
