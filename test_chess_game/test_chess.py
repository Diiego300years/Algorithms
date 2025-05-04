import pytest
from chess_game.chess import ChessBoard, CounterHandler

EXPECTED_EMPTY_BOARD = [
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', 8], 
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', 7],
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', 6], 
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', 5], 
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', 4], 
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', 3], 
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', 2], 
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', 1],
    ['A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ']
]


BOARD_WITH_COUNTERS = [
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', 8],
    ['♟️', '♟️', '♟️', '♟️', '♟️', '♟️', '♟️', '♟️', 7],
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', 6],
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', 5],
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', 4],
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', 3],
    ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', 2],
    ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', 1],
    ['A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H '] 
]

@pytest.fixture
def chess_board():
    return ChessBoard()

@pytest.fixture
def expected_board():
    return EXPECTED_EMPTY_BOARD

def test_create_board(chess_board, expected_board):
    assert chess_board._create_board() == expected_board


@pytest.fixture
def counter_handler():
    return CounterHandler()

@pytest.fixture
def board_with_counters():
    return BOARD_WITH_COUNTERS

def test_init_counters():
    pass


