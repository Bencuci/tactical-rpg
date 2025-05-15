import pygame
from tile import Tile
from units import Knight

class Grid:
    def __init__(self, tile_size, row_num, col_num, screen):
        self.tile_size = tile_size
        self.row_num = row_num 
        self.col_num = col_num
        self.screen = screen
        self.tiles = []
        self.selected_tile = None
        self.units = []
        self.selected_unit = None
        self.in_reach = []

        self._initialize_tiles()
        self.draw()
    
    def _initialize_tiles(self):
        for row in range(self.row_num):
            if row == len(self.tiles):
                self.tiles.append([])
            for col in range(self.col_num):
                tile = Tile(row, col)
                self.tiles[row].append(tile)
    
    def draw(self):
        for row in self.tiles:
            for tile in row:
                tile.color = "#ebdbb2"
                tile.border_color = "#282828"
                tile.border_width = 1
                posx = tile.col * self.tile_size
                posy = tile.row * self.tile_size
                rect = pygame.Rect(posx, posy, self.tile_size, self.tile_size)

                if self.selected_tile:
                    if self.selected_tile.unit and self.__is_within_reach(tile):
                        self.in_reach.append(tile)
                        tile.color = "#83a598"
                        tile.border_color = "#458588"
                    
                    if self.selected_tile.unit:
                        self.selected_tile.color = "#8ec07c"
                        self.selected_tile.border_color = "#8ec07c"
                        self.selected_tile.border_width = 3
                
                pygame.draw.rect(self.screen, tile.color, rect)
                pygame.draw.rect(self.screen, tile.border_color, rect, tile.border_width)
        
        for unit in self.units:
            x_center = (unit.col * self.tile_size) + (self.tile_size / 2)
            y_center = (unit.row * self.tile_size) + (self.tile_size / 2)

            pygame.draw.circle(self.screen, unit.color, (x_center, y_center), 25)
        

    def add_unit(self, unit, row, col):
        match unit.lower():
            case "knight":
                unit_to_add = Knight(row, col, self)
        
        self.tiles[row][col].occupied = True
        self.tiles[row][col].unit = unit_to_add
        self.units.append(unit_to_add)

        self.draw()
    
    def select_tile(self, row, col):
        self.in_reach = []

        if self.selected_tile and self.selected_tile == self.tiles[row][col]:
            self.selected_tile = None
        else:
            self.selected_tile = self.tiles[row][col]
            if self.selected_tile.unit:
                self.selected_unit = self.selected_tile.unit

        self.draw()
    
    def __is_within_reach(self, tile):
        x_dist = abs(tile.col - self.selected_tile.col)
        y_dist = abs(tile.row - self.selected_tile.row)

        if (x_dist + y_dist) <= self.selected_unit.movement:
            return True
        
        return False
