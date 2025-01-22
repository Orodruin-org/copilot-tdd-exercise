import pytest
from tetris.board import Board

def test_board_initialization():
    # Arrange / Act
    board = Board(rows=20, columns=10)

    # Assert
    assert board.rows == 20
    assert board.columns == 10
    assert len(board.grid) == 20
    assert len(board.grid[0]) == 10


def test_board_is_cell_empty():
    board = Board(rows=20, columns=10)

    # We expect an empty board initially
    assert board.is_cell_empty(0, 0) is True
    assert board.is_cell_empty(19, 9) is True

    # Let's assume placing a block at (0,0) will make it non-empty
    board.place_block(0, 0, "X")
    board.place_block(19, 9, "Y")
    assert board.is_cell_empty(0, 0) is False
    assert board.is_cell_empty(19, 9) is False

def test_board_initialization_edge_cases():
    # Test edge cases for board initialization
    with pytest.raises(ValueError):
        Board(rows=0, columns=10)
    with pytest.raises(ValueError):
        Board(rows=20, columns=0)
    with pytest.raises(ValueError):
        Board(rows=-1, columns=10)
    with pytest.raises(ValueError):
        Board(rows=20, columns=-1)

def test_board_is_cell_empty_edge_cases():
    board = Board(rows=20, columns=10)

    # Test edge cases for checking if a cell is empty
    with pytest.raises(IndexError):
        board.is_cell_empty(-1, 0)
    with pytest.raises(IndexError):
        board.is_cell_empty(20, 0)
    with pytest.raises(IndexError):
        board.is_cell_empty(0, -1)
    with pytest.raises(IndexError):
        board.is_cell_empty(0, 10)

def test_board_place_block_edge_cases():
    board = Board(rows=20, columns=10)

    # Test edge cases for placing a block
    with pytest.raises(IndexError):
        board.place_block(-1, 0, "X")
    with pytest.raises(IndexError):
        board.place_block(20, 0, "X")
    with pytest.raises(IndexError):
        board.place_block(0, -1, "X")
    with pytest.raises(IndexError):
        board.place_block(0, 10, "X")
