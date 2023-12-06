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
        first_row = board.create_first_row()
        assert first_row == " | | "
    
    def test_create_second_row(self):
        board = Board()
        second_row = board.create_second_row()
        assert second_row == " | | "
    
    def test_create_third_row(self):
        board = Board()
        third_row = board.create_third_row()
        assert third_row == " | | "
        
    def test_generate_board(self):
        board = Board()
        empty_board = board.generate_board()
        assert empty_board == " | | \n-----\n | | \n-----\n | | "