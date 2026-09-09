# Session 16 - everything that draws. The only file full of pygame.

import pygame
from config import *


def draw(screen, stars, ship):
    screen.fill(BG)

    for star in stars:
        pygame.draw.rect(screen, STAR_COLOUR, (star[0], star[1], STAR_SIZE, STAR_SIZE))

    pygame.draw.rect(screen, SHIP_COLOUR, (ship["x"], ship["y"], SHIP_W, SHIP_H))
