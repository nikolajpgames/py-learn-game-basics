# Session 17 - Press To Fire

import pygame
from config import *
from state import make_stars, make_ship, update_ship
from render import draw

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 17")
clock = pygame.time.Clock()

stars = make_stars()
ship = make_ship()

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---- ONE-OFF KEY PRESSES GO HERE ----------------------

        # -------------------------------------------------------

    keys = pygame.key.get_pressed()

    direction = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction = -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction = 1

    update_ship(ship, direction, dt)

    draw(screen, stars, ship)

    pygame.display.flip()

pygame.quit()
