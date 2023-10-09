from game.connect_checker import ConnectChecker
from game.constans_and_types import Color


class Board:
    def __init__(self):
        self.n_columns = 7
        self.n_rows = 6
        self.board = None
        self.reset_board()
        self.conn_checker = ConnectChecker(self)

    def reset_board(self):
        self.board = [[None for _ in range(self.n_columns)]
                      for _ in range(self.n_rows)]

    def calc_column_depth(self, col_nr: int):
        for row_nr in reversed(range(self.n_rows)):
            if self.board[row_nr][col_nr] is None:
                return row_nr
        return -1

    def insert_token(self, column_nr: int, player_color: Color):
        column_depth = self.calc_column_depth(column_nr)
        row_nr = column_depth
        self.board[row_nr][column_nr] = player_color
        self.conn_checker.are_four_connected(row_nr, column_nr)

    def __getitem__(self, row_nr: int):
        return self.board[row_nr]
