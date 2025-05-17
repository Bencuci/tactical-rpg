class Tile:
    def __init__(self, row, col, height=0, color="#ebdbb2", border_color="#282828", border_width=1):
        self.row = row
        self.col = col
        self.occupied = False
        self.unit = None
        self.trap = None
        self.height = height
        self.color = color
        self.border_color = border_color
        self.border_width = border_width