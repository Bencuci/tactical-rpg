import pygame
from tile import Tile

class Grid:
    def __init__(self, tile_size, row_num, col_num, screen):
        self._tile_size = tile_size
        self._row_num = row_num 
        self._col_num = col_num
        self._screen = screen
        self._tiles = []
        self._selected_tile = None

        self._initialize_tiles()
        self.draw()
    
    def _initialize_tiles(self):
        for row in range(self._row_num):
            if row == len(self._tiles):
                self._tiles.append([])
            for col in range(self._col_num):
                tile = Tile(row, col)
                self._tiles[row].append(tile)
    
    def draw(self):
        for row in self._tiles:
            for tile in row:
                posx = tile._col * self._tile_size
                posy = tile._row * self._tile_size
                rect = pygame.Rect(posx, posy, self._tile_size, self._tile_size)
                
                pygame.draw.rect(self._screen, tile._color, rect)
                pygame.draw.rect(self._screen, tile._border_color, rect, 1)
