import pytest

from display.types_and_constans import YELLOW_PLAYER_STYLE
from game.constans_and_types import RIGHT_ARROW, LEFT_ARROW, Color, EndOfGame
from game.game import Game


@pytest.fixture(scope="function")
def game():
    def pass_func(*args, **kwargs):
        pass

    class GameMock(Game):
        def __init__(self):
            self._get_players_names = pass_func
            super().__init__()
            self._player_style = YELLOW_PLAYER_STYLE
    return GameMock()


def test__move_token(game):
    game._token_col = 3
    game._move_token(RIGHT_ARROW)
    assert game._token_col == 4
    game._move_token(LEFT_ARROW)
    assert game._token_col == 3


def test__move_token__right_border(game):
    game._token_col = 6
    game._move_token(RIGHT_ARROW)
    assert game._token_col == 6


def test__move_token__left_border(game):
    game._token_col = 0
    game._move_token(LEFT_ARROW)
    assert game._token_col == 0


def test__try_to_insert_token(game):
    game._token_col = 2
    game._player_colour = Color.RED
    tokens_amount = game._inserted_tokens
    game._try_to_insert_token()
    assert game._board[5][2] == Color.RED
    assert game._inserted_tokens == tokens_amount + 1


def test__try_to_insert_token__full_column(game):
    for i in range(3):
        game._board[2 * i][2] = Color.YELLOW
        game._board[2 * i + 1][2] = Color.RED
    game._token_col = 2
    game._player_colour = Color.RED
    tokens_amount = game._inserted_tokens
    assert game._try_to_insert_token() is False
    assert game._inserted_tokens == tokens_amount


def test__increase_inserted_tokens(game):
    tokens_amount = 0
    for i in range(6*7 - 1):
        tokens_amount += 1
        game._increase_inserted_tokens()
        assert tokens_amount == game._inserted_tokens
    with pytest.raises(EndOfGame):
        game._increase_inserted_tokens()
