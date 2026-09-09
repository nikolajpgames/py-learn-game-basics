# Session 18 - everything that draws.

import pygame
from config import *


def draw(screen, stars, ship, shots):
    screen.fill(BG)

    for star in stars:
        pygame.draw.rect(screen, STAR_COLOUR, (star[0], star[1], STAR_SIZE, STAR_SIZE))

    for shot in shots:
        pygame.draw.rect(screen, SHOT_COLOUR, (shot["x"], shot["y"], SHOT_W, SHOT_H))

    pygame.draw.rect(screen, SHIP_COLOUR, (ship["x"], ship["y"], SHIP_W, SHIP_H))
