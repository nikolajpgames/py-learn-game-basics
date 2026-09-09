# Session 9 - Two Hundred Stars

import pygame

# ---- SETTINGS ----------------------------------
WIDTH = 800
HEIGHT = 450
FPS = 60
BG = (8, 9, 16)
STAR_SIZE = 2
STAR_COLOUR = (230, 230, 245)
STAR_COUNT = 200        # <-- today you actually make this many
# ------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 9")
clock = pygame.time.Clock()


# Where Session 8 left off: a list, but still typed out by hand.
# Fine for five stars. Hopeless for two hundred.
stars = [
    (100, 80),
    (400, 200),
    (650, 120),
    (220, 330),
    (540, 60),
]


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    # One loop draws however many stars are in the list.
    for star in stars:
        pygame.draw.rect(screen, STAR_COLOUR, (star[0], star[1], STAR_SIZE, STAR_SIZE))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
