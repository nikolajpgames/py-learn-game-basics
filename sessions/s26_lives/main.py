# Session 26 - Three Lives

import pygame
from config import *
from state import (make_bat, update_bat, make_ball, update_ball, bounce_off_bat,
                   make_bricks, overlaps, bounce_off_brick)
from render import draw

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 26")
clock = pygame.time.Clock()

bat = make_bat()
ball = make_ball()
bricks = make_bricks()

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    direction = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction = -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction = 1

    update_bat(bat, direction, dt)

    update_ball(ball, dt)

    bounce_off_bat(ball, bat)

    # a hit kills the brick and turns the ball around
    first_hit = None
    for brick in bricks:
        if overlaps(ball, brick):
            brick["gone"] = True
            if first_hit is None:
                first_hit = brick

    if first_hit is not None:
        bounce_off_brick(ball, first_hit)

    kept = []
    for brick in bricks:
        if "gone" not in brick:
            kept.append(brick)
    bricks = kept

    # ---- NOTHING HAPPENS WHEN THE BALL IS LOST ---------------

    # ---------------------------------------------------------

    draw(screen, bat, ball, bricks)

    pygame.display.flip()

pygame.quit()
