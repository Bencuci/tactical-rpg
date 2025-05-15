from .unit import Unit

class Knight(Unit):
    def __init__(self, row, col, grid):
        super().__init__(row, col, 100, 15, 8, 2, 1, grid)