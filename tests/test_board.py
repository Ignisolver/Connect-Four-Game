import pytest

from game.board import Board
from game.constans_and_types import Color


@pytest.fixture(scope="function")
def board():
    return Board()


def test_reset_board__set_size_ok(board):
    _ = board[5][6]
    with pytest.raises(IndexError):
        _ = board[6][6]
    with pytest.raises(IndexError):
        _ = board[6][7]


def test_calc_column_depth(board):
    assert board.calc_column_depth(2) == 5
    board.insert_token(2, Color.YELLOW)
    board.insert_token(2, Color.YELLOW)
    assert board.calc_column_depth(2) == 3
    for i in range(3):
        board.insert_token(2, Color.RED)
    board.insert_token(2, Color.YELLOW)
    assert board.calc_column_depth(2) == -1


def test_insert_token_same_column(board):
    board.insert_token(3, Color.YELLOW)
    board.insert_token(3, Color.RED)
    board.insert_token(3, Color.YELLOW)
    assert board[5][3] == Color.YELLOW
    assert board[4][3] == Color.RED
    assert board[3][3] == Color.YELLOW
    assert board[2][3] is None


def test_insert_token_different_rows(board):
    board.insert_token(1, Color.YELLOW)
    board.insert_token(2, Color.RED)
    board.insert_token(3, Color.YELLOW)
    assert board[5][1] == Color.YELLOW
    assert board[5][2] == Color.RED
    assert board[5][3] == Color.YELLOW

