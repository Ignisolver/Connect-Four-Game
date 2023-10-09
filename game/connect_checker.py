from game.constans_and_types import EndOfGame


class ConnectChecker:
    def __init__(self, board):
        self.board = board
        self.last_row = None
        self.last_col = None
        self.player_color = None
        self.min_col = None
        self.max_col = None
        self.min_row = None
        self.max_row = None

    def are_four_connected(self, last_row: int, last_col: int):
        self.last_row = last_row
        self.last_col = last_col
        self.player_color = self.board[last_row][last_col]
        self.min_col = max(0, self.last_col - 3)
        self.max_col = min(self.board.n_columns - 1, self.last_col + 3)
        self.min_row = max(0, self.last_row - 3)
        self.max_row = min(self.board.n_rows - 1, self.last_row + 3)
        self._are_four_connected()

    def _count_connections(self, row_step, col_step):
        col = self.last_col
        row = self.last_row
        connected = 0
        for _ in range(3):
            col += col_step
            row += row_step
            if ((self.min_col > col) or (col > self.max_col) or
                    (self.min_row > row) or (row > self.max_row)):
                break
            else:
                if self.board[row][col] == self.player_color:
                    connected += 1
                else:
                    break
        return connected

    def _are_four_connected(self):
        for row_step, col_step in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
            connected = 0
            connected += self._count_connections(row_step, col_step)
            connected += self._count_connections(-row_step, -col_step)
            if connected >= 3:
                raise EndOfGame(player=self.player_color)
