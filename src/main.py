import pygame
from constants import *
from grid import Grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True

    grid = Grid(TILE_SIZE, ROW_NUM, COL_NUM, screen)
    grid.add_unit("knight", 3, 3)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = pygame.mouse.get_pos()
                    row = my // TILE_SIZE
                    col = mx // TILE_SIZE
                    grid.select_tile(row, col)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()