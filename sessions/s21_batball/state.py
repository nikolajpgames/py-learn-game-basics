# Arkanoid - the rules of the world. No pygame in here.

from config import *


def make_bat():
    bat = {
        "x": WIDTH / 2 - BAT_W / 2,
        "y": BAT_Y,
        "w": BAT_W,
        "h": BAT_H,
    }
    return bat


def update_bat(bat, direction, dt):
    bat["x"] = bat["x"] + direction * BAT_SPEED * dt

    if bat["x"] < 0:
        bat["x"] = 0
    if bat["x"] + bat["w"] > WIDTH:
        bat["x"] = WIDTH - bat["w"]


# ---- YOUR BALL FUNCTIONS GO HERE -----------------------------
