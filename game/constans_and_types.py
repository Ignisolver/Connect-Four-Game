from enum import Enum

NAME_INPUT_STR = "Enter the name of player {color} >>>"
NAME_LIMIT_STR = "Please enter the name with less then 20 characters"

ENTER = "\n"
QUIT_KEY = 27
RIGHT_ARROW = "KEY_RIGHT"
LEFT_ARROW = "KEY_LEFT"
MAX_TOKEN_AMOUNT = 42


class EndOfGame(Exception):
    def __init__(self, player=None):
        self.player_color = player
        super().__init__()


class Color(Enum):
    RED = "RED"
    YELLOW = "YELLOW"


COLORS = (Color.RED, Color.YELLOW)
