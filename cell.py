'''This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.'''
class Cell:
    def __init__(self, value, row, col, screen):
        pass
    def set_cell_value(self, value):
        pass
    def set_sketched_value(self, value):
        pass
    def draw(self):
        pass

        '''Draws this cell, along with the value inside it.
    If this cell has a nonzero value, that value is displayed.
    Otherwise, no value is displayed in the cell.
    The cell is outlined red if it is currently selected'''
