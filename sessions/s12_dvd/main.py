# Session 12 - The DVD Bouncer

import pygame

# ---- SETTINGS ----------------------------------
WIDTH = 800
HEIGHT = 450
FPS = 60
BG = (12, 13, 26)
BOX_COLOUR = (61, 225, 225)
BOX_SIZE = 40
SPEED = 240       # pixels per second
# ------------------------------------------------


def update(x, y, vx, vy, dt):
    x = x + vx * dt
    y = y + vy * dt

    # ---- YOUR WALL CHECKS GO HERE --------------

    # --------------------------------------------

    return x, y, vx, vy


def draw(screen, x, y):
    screen.fill(BG)
    pygame.draw.rect(screen, BOX_COLOUR, (x, y, BOX_SIZE, BOX_SIZE))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 12")
clock = pygame.time.Clock()

box_x = 100.0
box_y = 60.0
box_vx = SPEED
box_vy = SPEED

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    box_x, box_y, box_vx, box_vy = update(box_x, box_y, box_vx, box_vy, dt)
    draw(screen, box_x, box_y)

    pygame.display.flip()

pygame.quit()
