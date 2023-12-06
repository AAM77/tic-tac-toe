import pytest
from src.board import *

class TestBoard:
    def test_board_class_exists(self):
        board = Board()
        assert board
        
    def test_generate_board_positions(self):
        board = Board()
        assert len(board.generate_board_positions()) == 9
    
    def test_create_first_row(self):
        board = Board()
        first_row: str = board.create_row(0, 3)
        assert first_row == " | | "
    
    def test_create_second_row(self):
        board = Board()
        second_row: str = board.create_row(3, 6)
        assert second_row == " | | "
    
    def test_create_third_row(self):
        board = Board()
        third_row: str = board.create_row(6, 9)
        assert third_row == " | | "
        
    def test_generate_board(self):
        board = Board()
        empty_board: str = board.generate_board()
        assert empty_board == " | | \n-----\n | | \n-----\n | | "
    
    def test_initialize_with_empty_positions(self):
        board = Board()
        assert all(position == " " for position in board.positions)
        assert len(board.positions) == 9
    
    def test_board_with_occupied_positions(self):
        board = Board()
        board.positions: list[str] = [' ', 'X', ' ', 'O', ' ', 'O', ' ', ' ', 'X']
        occupied_board: str = board.generate_board()
        assert occupied_board == " |X| \n-----\nO| |O\n-----\n | |X"
