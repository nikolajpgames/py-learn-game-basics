# Session 15 - Three Files
#
# Everything is in this one file. By the end of today it will be in four,
# and this one will be short enough to read in a single glance.

import pygame
import random

# ---- SETTINGS ----------------------------------
WIDTH = 800
HEIGHT = 450
FPS = 60
BG = (12, 13, 26)
BOX_COLOUR = (61, 225, 225)
HIT_COLOUR = (248, 87, 193)
BOX_SIZE = 40
BOX_COUNT = 20
SPEED = 150
# ------------------------------------------------


def overlaps(a, b):
    if a["x"] + BOX_SIZE < b["x"]:
        return False
    if b["x"] + BOX_SIZE < a["x"]:
        return False
    if a["y"] + BOX_SIZE < b["y"]:
        return False
    if b["y"] + BOX_SIZE < a["y"]:
        return False
    return True


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


def make_boxes():
    boxes = []

    for i in range(BOX_COUNT):
        box = {
            "x": float(random.randint(0, WIDTH - BOX_SIZE)),
            "y": float(random.randint(0, HEIGHT - BOX_SIZE)),
            "vx": random.choice([-SPEED, SPEED]),
            "vy": random.choice([-SPEED, SPEED]),
            "colour": BOX_COLOUR,
        }
        boxes.append(box)

    return boxes


def draw(screen, boxes):
    screen.fill(BG)

    for box in boxes:
        pygame.draw.rect(screen, box["colour"], (box["x"], box["y"], BOX_SIZE, BOX_SIZE))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Session 15")
clock = pygame.time.Clock()

boxes = make_boxes()

running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for box in boxes:
        update(box, dt)

    for box in boxes:
        box["colour"] = BOX_COLOUR

    for a in boxes:
        for b in boxes:
            if a is not b and overlaps(a, b):
                a["colour"] = HIT_COLOUR

    draw(screen, boxes)

    pygame.display.flip()

pygame.quit()
