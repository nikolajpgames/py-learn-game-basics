# Session 28 - More Levels

import pygame
from config import *
from state import (make_bat, update_bat, make_ball, update_ball, bounce_off_bat,
                   overlaps, bounce_off_brick, load_level)
from render import draw

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 28")
clock = pygame.time.Clock()

bat = make_bat()
ball = make_ball()
bricks = load_level("level01.txt")
lives = START_LIVES
mode = "playing"

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and mode == "over":
                bricks = load_level("level01.txt")
                ball = make_ball()
                lives = START_LIVES
                mode = "playing"

    keys = pygame.key.get_pressed()

    direction = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction = -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction = 1

    if mode == "playing":

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

        # ---- NOTHING HAPPENS WHEN THE WALL IS CLEARED ------------

        # ---------------------------------------------------------

        if ball["y"] > HEIGHT:
            lives = lives - 1
            ball = make_ball()
            if lives == 0:
                mode = "over"

    draw(screen, bat, ball, bricks, lives, mode)

    pygame.display.flip()

pygame.quit()
