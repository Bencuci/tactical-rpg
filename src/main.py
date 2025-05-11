import pygame
from constants import *
from grid import Grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True

    grid = Grid(TILE_SIZE, ROW_NUM, COL_NUM, screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            print(mx // TILE_SIZE, my // TILE_SIZE)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()