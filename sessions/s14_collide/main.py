# Session 14 - When Boxes Meet

import pygame
import random

# ---- SETTINGS ----------------------------------
WIDTH = 800
HEIGHT = 450
FPS = 60
BG = (12, 13, 26)
BOX_COLOUR = (61, 225, 225)
HIT_COLOUR = (248, 87, 193)
BOX_SIZE = 70
BOX_COUNT = 6
SPEED = 150
# ------------------------------------------------


def update(box, dt):
    box["x"] = box["x"] + box["vx"] * dt
    box["y"] = box["y"] + box["vy"] * dt

    if box["x"] < 0:
        box["vx"] = -box["vx"]
    if box["x"] + BOX_SIZE > WIDTH:
        box["vx"] = -box["vx"]
    if box["y"] < 0:
        box["vy"] = -box["vy"]
    if box["y"] + BOX_SIZE > HEIGHT:
        box["vy"] = -box["vy"]


def draw(screen, box):
    pygame.draw.rect(screen, BOX_COLOUR, (box["x"], box["y"], BOX_SIZE, BOX_SIZE))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 14")
clock = pygame.time.Clock()

boxes = []

for i in range(BOX_COUNT):
    box = {
        "x": float(random.randint(0, WIDTH - BOX_SIZE)),
        "y": float(random.randint(0, HEIGHT - BOX_SIZE)),
        "vx": random.choice([-SPEED, SPEED]),
        "vy": random.choice([-SPEED, SPEED]),
    }
    boxes.append(box)

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for box in boxes:
        update(box, dt)

    screen.fill(BG)

    for box in boxes:
        draw(screen, box)

    pygame.display.flip()

pygame.quit()
