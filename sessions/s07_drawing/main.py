# Session 7 - Drawing By Numbers

import pygame

# ---- SETTINGS ----------------------------------
WIDTH = 800
HEIGHT = 450
FPS = 60
BG = (20, 22, 34)
# ------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 7")
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    # ---- YOUR DRAWING GOES HERE ----------------
    pygame.draw.rect(screen, (61, 225, 225), (100, 80, 120, 60))
    # --------------------------------------------

    pygame.display.flip()

    # Hold the loop at a steady speed instead of running flat out.
    clock.tick(FPS)

pygame.quit()
