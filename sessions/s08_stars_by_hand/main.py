# Session 8 - Three Stars By Hand

import pygame

# ---- SETTINGS ----------------------------------
WIDTH = 800
HEIGHT = 450
FPS = 60
BG = (8, 9, 16)
STAR_SIZE = 5
STAR_COLOUR = (230, 230, 245)
# ------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 8")
clock = pygame.time.Clock()


# Three stars, written out one at a time.
# Each one is a TUPLE: an x and a y glued together with round brackets.
star1 = (100, 80)
star2 = (400, 200)
star3 = (650, 120)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    # One draw line for every single star.
    # Read them carefully - they are almost identical.
    pygame.draw.rect(screen, STAR_COLOUR, (star1[0], star1[1], STAR_SIZE, STAR_SIZE))
    pygame.draw.rect(screen, STAR_COLOUR, (star2[0], star2[1], STAR_SIZE, STAR_SIZE))
    pygame.draw.rect(screen, STAR_COLOUR, (star3[0], star3[1], STAR_SIZE, STAR_SIZE))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
