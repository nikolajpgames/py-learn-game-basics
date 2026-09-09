# Session 23 - A Wall Of Bricks

import pygame
from config import *
from state import make_bat, update_bat, make_ball, update_ball, bounce_off_bat
from render import draw

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 23")
clock = pygame.time.Clock()

bat = make_bat()
ball = make_ball()

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

    # ---- THE BRICKS GO HERE ----------------------------------

    # ---------------------------------------------------------

    draw(screen, bat, ball)

    pygame.display.flip()

pygame.quit()
