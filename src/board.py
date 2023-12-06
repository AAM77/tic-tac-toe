class Board:
        
    def generate_board_positions(self):
        return [" "]*9
    
    def create_first_row(self):
        return "|".join(self.generate_board_positions()[:3])
    
    def create_second_row(self):
        return "|".join(self.generate_board_positions()[3:6])
    
    def create_third_row(self):
        return "|".join(self.generate_board_positions()[6:9])
    
    def generate_board(self):
        first_row = self.create_first_row()
        second_row = self.create_second_row()
        third_row = self.create_third_row()
        divider = "-----"
        board = "\n".join([first_row, divider, second_row, divider, third_row])
        return board