# Session 16 - Your Ship

import pygame
from config import *
from state import make_stars, make_ship, update_ship
from render import draw

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 16")
clock = pygame.time.Clock()

stars = make_stars()
ship = make_ship()

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- WHICH WAY IS THE PLAYER PUSHING? --------------------
    # Nothing reads the keyboard yet, so the ship never moves.
    direction = 0
    # -----------------------------------------------------------

    update_ship(ship, direction, dt)

    draw(screen, stars, ship)

    pygame.display.flip()

pygame.quit()
