# Session 11 - Real Speed

import pygame

# ---- SETTINGS ----------------------------------
WIDTH = 800
HEIGHT = 450
FPS = 60
BG = (20, 22, 34)
BOX_COLOUR = (61, 225, 225)
BOX_SIZE = 40
STEP = 4          # pixels per FRAME  <-- today you fix this
# ------------------------------------------------


def update(x, y):
    x = x + STEP
    return x, y


def draw(screen, x, y):
    screen.fill(BG)
    pygame.draw.rect(screen, BOX_COLOUR, (x, y, BOX_SIZE, BOX_SIZE))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 11")
clock = pygame.time.Clock()

box_x = 100
box_y = 200

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    box_x, box_y = update(box_x, box_y)
    draw(screen, box_x, box_y)

    pygame.display.flip()

pygame.quit()
