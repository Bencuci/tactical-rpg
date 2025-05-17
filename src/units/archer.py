from .unit import Unit

class Archer(Unit):
    def __init__(self, row, col, grid):
        super().__init__(row, col, 40, 12, 5, 3, 5, grid)
        self.name = "Archer"
        self.color = "#fabd2f"