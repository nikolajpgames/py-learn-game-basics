# Session 19 - the rules of the world. No pygame in here.

import random
from config import *


def make_stars():
    stars = []
    for i in range(STAR_COUNT):
        stars.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))
    return stars


def make_ship():
    return {"x": WIDTH / 2 - SHIP_W / 2, "y": HEIGHT - SHIP_H - 20}


def update_ship(ship, direction, dt):
    ship["x"] = ship["x"] + direction * SHIP_SPEED * dt

    if ship["x"] < 0:
        ship["x"] = 0
    if ship["x"] + SHIP_W > WIDTH:
        ship["x"] = WIDTH - SHIP_W


def make_shot(ship):
    return {"x": ship["x"] + SHIP_W / 2 - SHOT_W / 2, "y": ship["y"]}


def update_shots(shots, dt):
    kept = []

    for shot in shots:
        shot["y"] = shot["y"] - SHOT_SPEED * dt
        if shot["y"] + SHOT_H > 0:
            kept.append(shot)

    return kept


def make_targets():
    targets = []

    for i in range(TARGET_COUNT):
        target = {
            "x": float(random.randint(0, WIDTH - TARGET_W)),
            "y": float(random.randint(20, 160)),
            "vx": random.choice([-TARGET_SPEED, TARGET_SPEED]),
            "w": TARGET_W,
            "h": TARGET_H,
        }
        targets.append(target)

    return targets


def update_targets(targets, dt):
    for target in targets:
        target["x"] = target["x"] + target["vx"] * dt

        if target["x"] < 0:
            target["vx"] = -target["vx"]
        if target["x"] + target["w"] > WIDTH:
            target["vx"] = -target["vx"]


# ---- YOUR COLLISION CHECK GOES HERE --------------------------
