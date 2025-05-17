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
        self.in_reach = [] # Movement range
        self.in_range = [] # Attack range

        self._initialize_tiles()
        self.select_tile(0, 0)
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
                posx = tile.col * self.tile_size
                posy = tile.row * self.tile_size
                rect = pygame.Rect(posx, posy, self.tile_size, self.tile_size)

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
        # if clicked on already selected tile again
        if self.selected_tile and self.selected_tile == self.tiles[row][col] and self.selected_unit:
            self.selected_tile = None
            self.selected_unit = None
        else:
            self.selected_tile = self.tiles[row][col]
            if self.selected_tile.unit and not self.selected_unit:
                self.selected_unit = self.selected_tile.unit
                    

            
        if self.selected_unit:
            if self.selected_tile.unit and self.__is_within_range(self.selected_tile.unit):
                self.__attack_unit(self.selected_unit, self.selected_tile.unit)
                self.selected_unit = None

            elif not self.selected_tile.unit and self.__is_within_reach(self.selected_tile):
                self.__move_unit(self.selected_unit, self.selected_tile.row, self.selected_tile.col)
                self.in_reach = []
                self.in_range = []
                self.selected_unit = None

            elif not self.selected_tile.unit:
                self.selected_unit = None

        for row in self.tiles:
            for tile in row:
                tile.color = "#ebdbb2"
                tile.border_color = "#282828"
                tile.border_width = 1
                
                if self.selected_unit:
                    if self.__is_within_range(tile) and tile.unit:
                        self.in_range.append(tile)
                        tile.color = "#fe8019"
                        tile.border_color = "#d65d0e"
                    if self.__is_within_reach(tile) and not tile.unit:
                        self.in_reach.append(tile)
                        tile.color = "#83a598"
                        tile.border_color = "#458588"

                if self.selected_tile and self.selected_tile.unit:
                    self.selected_tile.color = "#8ec07c"
                    self.selected_tile.border_color = "#8ec07c"
                    self.selected_tile.border_width = 3
                    

        if self.selected_unit:
            print(f"selected_unit: {self.selected_unit.col}, {self.selected_unit.row}")
        if self.selected_tile:
            print(f"selected_tile: {self.selected_tile.col}, {self.selected_tile.row}")
        self.draw()
        if self.selected_unit:
            print(f"selected_unit: {self.selected_unit.col}, {self.selected_unit.row}")
        if self.selected_tile:
            print(f"selected_tile: {self.selected_tile.col}, {self.selected_tile.row}")
    
    def __is_within_reach(self, tile):
        x_dist = abs(tile.col - self.selected_unit.col)
        y_dist = abs(tile.row - self.selected_unit.row)

        if 0 < (x_dist + y_dist) <= self.selected_unit.movement:
            return True
        
        return False

    def __is_within_range(self, target):
        x_dist = abs(target.col - self.selected_unit.col)
        y_dist = abs(target.row - self.selected_unit.row)

        if 0 < (x_dist + y_dist) <= self.selected_unit.range:
            return True

        return False

    def __move_unit(self, unit, row, col):
        self.tiles[unit.row][unit.col].occupied = False
        self.tiles[unit.row][unit.col].unit = None
        self.tiles[row][col].occupied = True
        self.tiles[row][col].unit = unit
        unit.row = row
        unit.col = col
        self.selected_unit = None

    def __remove_unit(self, unit):
        self.tiles[unit.row][unit.col].occupied = False
        self.tiles[unit.row][unit.col].unit = None
        self.units.remove(unit)

    def __attack_unit(self, unit, target):
        target.hp -= unit.att - target.defence

        print(f"{unit.col}, {unit.row} attacking {target.col}, {target.row}")

        if target.hp <= 0:
            target.hp = 0
            self.__remove_unit(target)
        
        print(target.hp)

        self.selected_unit = None