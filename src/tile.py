from constants import *

class Tile:
    def __init__(self, row, col, height=0, color="white", border_color="black"):
        self._row = row
        self._col = col
        self._color = color
        self._border_color = border_color
        self._occupied = False
        self._unit = None
        self._trap = None
        self._height = height