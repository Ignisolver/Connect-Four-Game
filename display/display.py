import curses

from display.types_and_constans import (X_SHIFT, BOARD_STYLE, Style,
                                        TURN, EMPTY_STYLE, INSTRUCTIONS,
                                        WIN_STR, DRAW_STR, initialize_styles)


class BoardDisplayer:
    def __init__(self):
        self.std_scr = None
        self._init_curses()
        self._row_len = 44
        self._col_len = 19
        self._box_row_len = 4
        self._box_col_len = 2
        self._box_with_border_row_len = 6
        self._box_with_border_col_len = 3
        self.reset_board()

    def _init_curses(self):
        self.std_scr = curses.initscr()
        curses.start_color()
        curses.curs_set(0)
        initialize_styles()
        curses.noecho()
        self.std_scr.keypad(True)

    def reset_board(self):
        self.std_scr.clear()
        self._draw_board()
        self._print_during_game_instructions()

    def _refresh(self):
        self.std_scr.refresh()

    def _add_horizontal_crossbar(self, row):
        self.std_scr.addstr(row + X_SHIFT, 0, self._row_len * BOARD_STYLE.char,
                            BOARD_STYLE.color)

    def _add_vertical_crossbar(self, col):
        for r in range(self._col_len):
            self.std_scr.addstr(r + X_SHIFT, col, BOARD_STYLE.char,
                                BOARD_STYLE.color)

    def _draw_horizontal_crossbars(self):
        for row_nr in range(self._col_len):
            if row_nr % self._box_with_border_col_len == 0:
                self._add_horizontal_crossbar(row_nr)

    def _draw_vertical_crossbars(self):
        for col_nr in range(self._row_len):
            if (col_nr % self._box_with_border_row_len == 1 or
                    (col_nr + 1) % self._box_with_border_row_len == 1):
                self._add_vertical_crossbar(col_nr)

    def draw_box(self, row: int, col: int, style: Style):
        """
       Colors box in the board
       :param row: int in range -1 to 6, -1 for box above the board
       :param col: int in range 0 to 6
       :param style: EMPTY or (RED or YELLOW PLAYER) STYLE
       :return: None
       """
        row_nr = (row + 1) * self._box_with_border_col_len + 1
        col_nr = col * self._box_with_border_row_len + 2
        for r in range(row_nr, row_nr + self._box_col_len):
            for c in range(col_nr, col_nr + self._box_row_len):
                self.std_scr.addstr(r, c, style.char, style.color)
        self._refresh()

    def _draw_board(self):
        self._draw_horizontal_crossbars()
        self._draw_vertical_crossbars()
        self._refresh()

    def _clear_upper_text(self):
        self.std_scr.addstr(0, 0, 100 * " ", EMPTY_STYLE.color)

    def print_turn(self, name):
        self._clear_upper_text()
        self.std_scr.addstr(0, 0, TURN.format(name=name))
        self._refresh()

    def _print_during_game_instructions(self):
        start_row = self._col_len + X_SHIFT + 1
        self.std_scr.addstr(start_row, 0, INSTRUCTIONS)

    def print_win_end(self, player):
        self._clear_upper_text()
        self.std_scr.addstr(0, 0, WIN_STR.format(player=player))

    def print_draw_end(self):
        self._clear_upper_text()
        self.std_scr.addstr(0, 0, DRAW_STR)
