# Session 20 - Score And Game Over

import pygame
from config import *
from state import (make_stars, make_ship, update_ship, make_shot,
                   update_shots, make_targets, update_targets, overlaps)
from render import draw

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 20")
clock = pygame.time.Clock()

stars = make_stars()
ship = make_ship()
shots = []
targets = make_targets()

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
    shots = update_shots(shots, dt)
    update_targets(targets, dt)

    # a hit kills the shot and the target it hit
    for shot in shots:
        for target in targets:
            if overlaps(shot, target):
                shot["hit"] = True
                target["hit"] = True

    kept_shots = []
    for shot in shots:
        if "hit" not in shot:
            kept_shots.append(shot)
    shots = kept_shots

    kept_targets = []
    for target in targets:
        if "hit" not in target:
            kept_targets.append(target)
    targets = kept_targets

    # ---- NOTHING KEEPS SCORE YET --------------------------------

    # --------------------------------------------------------------

    draw(screen, stars, ship, shots, targets)

    pygame.display.flip()

pygame.quit()
