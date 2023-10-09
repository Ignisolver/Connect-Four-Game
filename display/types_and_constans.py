import curses
from dataclasses import dataclass


@dataclass
class Style:
    char: str
    color = None


TURN = "TURN: {name}"
INSTRUCTIONS = "USE RIGHT AND LEFT ARROWS TO CHANGE TOKEN POSITION\n" \
               "PRESS ENTER TO THROW"
CONTINUE_STR = "     PRESS ESCAPE TO QUIT OR ANY ANOTHER KEY TO CONTINUE"
WIN_STR = "PLAYER {player} WON !!!" + CONTINUE_STR
DRAW_STR = "NO ONE WON - A DRAW !!!" + CONTINUE_STR
PLAYER_NAME_INPUT = "Type {color} player name and press ENTER >>> "

X_SHIFT = 3

HASH = "#"
BOARD_STYLE = Style(HASH)

SPACE = " "
EMPTY_STYLE = Style(SPACE)

PLUS = "+"
RED_PLAYER_STYLE = Style(PLUS)

O_LETTER = "o"
YELLOW_PLAYER_STYLE = Style(O_LETTER)


def initialize_styles():
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
    board_color = curses.color_pair(1)
    BOARD_STYLE.color = board_color

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLACK)
    empty_space_color = curses.color_pair(2)
    EMPTY_STYLE.color = empty_space_color

    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)
    red_player_color = curses.color_pair(3)
    RED_PLAYER_STYLE.color = red_player_color

    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    yellow_player_color = curses.color_pair(4)
    YELLOW_PLAYER_STYLE.color = yellow_player_color
