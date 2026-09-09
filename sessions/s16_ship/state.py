# Session 16 - the rules of the world.
# No pygame in this file. It knows nothing about pixels or keyboards.

import random
from config import *


def make_stars():
    stars = []

    for i in range(STAR_COUNT):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        stars.append((x, y))

    return stars


def make_ship():
    ship = {
        "x": WIDTH / 2 - SHIP_W / 2,
        "y": HEIGHT - SHIP_H - 20,
    }
    return ship


def update_ship(ship, direction, dt):
    # direction is -1 for left, 1 for right, 0 for not moving.
    # Notice this function has no idea which keys those came from.
    ship["x"] = ship["x"] + direction * SHIP_SPEED * dt
