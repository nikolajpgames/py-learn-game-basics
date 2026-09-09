# Session 17 - the rules of the world. Still no pygame in here.

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
    ship["x"] = ship["x"] + direction * SHIP_SPEED * dt

    if ship["x"] < 0:
        ship["x"] = 0
    if ship["x"] + SHIP_W > WIDTH:
        ship["x"] = WIDTH - SHIP_W


# ---- YOUR NEW FUNCTIONS GO HERE ------------------------------
