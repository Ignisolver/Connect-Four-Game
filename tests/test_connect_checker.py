import pytest

from game.board import Board
from game.connect_checker import ConnectChecker
from game.constans_and_types import Color, EndOfGame


@pytest.fixture(scope="function")
def board():
    return Board()


def test_are_four_connected__vertically(board):
    for i in range(1, 5):
        board[4][i] = Color.YELLOW
    c = ConnectChecker(board)
    for i in range(1, 5):
        with pytest.raises(EndOfGame):
            c.are_four_connected(4, i)


def test_are_four_connected__horizontally(board):
    for i in range(1, 5):
        board[i][3] = Color.YELLOW
    c = ConnectChecker(board)
    for i in range(1, 5):
        with pytest.raises(EndOfGame):
            c.are_four_connected(i, 3)


def test_are_four_connected__back_diagonal(board):
    for i in range(1, 5):
        board[i][i] = Color.YELLOW
    c = ConnectChecker(board)
    for i in range(1, 5):
        with pytest.raises(EndOfGame):
            c.are_four_connected(i, i)


def test_are_four_connected__forward_diagonal(board):
    for i in range(1, 5):
        board[5-i][5-i] = Color.YELLOW
    c = ConnectChecker(board)
    for i in range(1, 5):
        with pytest.raises(EndOfGame):
            c.are_four_connected(5-i, 5-i)


def test_are_four_connected__not_connected(board):
    for i in range(1, 4):
        board[i][i] = Color.YELLOW
    board[4][4] = Color.RED
    c = ConnectChecker(board)
    c.are_four_connected(4, 4)
    