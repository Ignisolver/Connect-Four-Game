from itertools import cycle

from display.display import BoardDisplayer
from display.types_and_constans import (RED_PLAYER_STYLE, YELLOW_PLAYER_STYLE,
                                        EMPTY_STYLE, PLAYER_NAME_INPUT)
from game.board import Board
from game.constans_and_types import (Color, ENTER, RIGHT_ARROW, LEFT_ARROW,
                                     EndOfGame, COLORS, MAX_TOKEN_AMOUNT,
                                     QUIT_KEY)


class Game:
    def __init__(self):
        self._board = Board()
        self._players_names = dict()
        self._get_players_names()
        self._player_styles = {Color.RED: RED_PLAYER_STYLE,
                               Color.YELLOW: YELLOW_PLAYER_STYLE}
        self._displayer = BoardDisplayer()
        self._player_colour = None
        self._token_col = None
        self._player_style = None
        self._player_name = None
        self._inserted_tokens = 0

    def _get_players_names(self):
        for color in COLORS:
            name = input(PLAYER_NAME_INPUT.format(color=color.value))
            self._players_names[color] = name

    def start_game(self):
        while True:
            try:
                self._single_play()
            except EndOfGame as e:
                winner_color = e.player_color
                self._print_end_of_the_play(winner_color)
            key = self._displayer.std_scr.getch()
            if key == QUIT_KEY:
                break

    def _print_end_of_the_play(self, winner_color):
        if winner_color is None:
            self._displayer.print_draw_end()
        else:
            player_name = self._players_names[winner_color]
            self._displayer.print_win_end(player_name)

    def _reset_game(self):
        self._board.reset_board()
        self._displayer.reset_board()

    def _single_play(self):
        self._reset_game()
        for player_colour in cycle(COLORS):
            self._player_colour = player_colour
            self._init_turn()
            while True:
                key = self._displayer.std_scr.getkey()
                if key == ENTER:
                    success = self._try_to_insert_token()
                    if success:
                        break
                    else:
                        continue
                else:
                    self._move_token(key)

    def _move_token(self, key):
        self._displayer.draw_box(-1, self._token_col, EMPTY_STYLE)
        if key == RIGHT_ARROW:
            self._token_col = min(self._board.n_columns - 1, self._token_col + 1)
        elif key == LEFT_ARROW:
            self._token_col = max(0, self._token_col - 1)
        self._displayer.draw_box(-1, self._token_col, self._player_style)

    def _init_turn(self):
        self._player_name = self._players_names[self._player_colour]
        self._displayer.print_turn(self._player_name)
        self._player_style = self._player_styles[self._player_colour]
        self._token_col = 3
        self._displayer.draw_box(-1, self._token_col, self._player_style)

    def _try_to_insert_token(self):
        col_depth = self._board.calc_column_depth(self._token_col)
        if col_depth == -1:
            return False
        else:
            self._insert_token(col_depth)
            return True

    def _increase_inserted_tokens(self):
        self._inserted_tokens += 1
        if self._inserted_tokens == MAX_TOKEN_AMOUNT:
            raise EndOfGame()

    def _insert_token(self, col_depth):
        self._displayer.draw_box(-1, self._token_col, EMPTY_STYLE)
        self._displayer.draw_box(col_depth, self._token_col, self._player_style)
        self._board.insert_token(self._token_col, self._player_colour)
        self._increase_inserted_tokens()
