class Board:
    
    def __init__(self):
        self.positions = self.generate_board_positions()
        
    def generate_board_positions(self) -> list[str]:
        return [" "]*9
    
    def create_row(self, starting_index: int, ending_index: int) -> str:
        return "|".join(self.positions[starting_index:ending_index])
    
    def generate_board(self) -> str:
        first_row: str = self.create_row(0, 3)
        second_row: str = self.create_row(3, 6)
        third_row: str = self.create_row(6, 9)
        divider: str = "-----"
        board: str = "\n".join([first_row, divider, second_row, divider, third_row])
        return board
