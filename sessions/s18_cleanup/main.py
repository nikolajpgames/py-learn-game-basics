# Session 18 - Cleaning Up

import pygame
from config import *
from state import make_stars, make_ship, update_ship, make_shot, update_shots
from render import draw

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 18")
clock = pygame.time.Clock()

stars = make_stars()
ship = make_ship()
shots = []

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shots.append(make_shot(ship))

    keys = pygame.key.get_pressed()

    direction = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction = -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction = 1

    update_ship(ship, direction, dt)
    update_shots(shots, dt)

    # ---- NOTHING EVER THROWS THE OLD SHOTS AWAY ----------------

    # -------------------------------------------------------------

    draw(screen, stars, ship, shots)

    pygame.display.flip()

pygame.quit()
