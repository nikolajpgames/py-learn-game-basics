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


def make_ball():
    ball = {
        "x": WIDTH / 2 - BALL_SIZE / 2,
        "y": BAT_Y - 120,
        "w": BALL_SIZE,
        "h": BALL_SIZE,
        "vx": BALL_SPEED,
        "vy": -BALL_SPEED,
    }
    return ball


def update_ball(ball, dt):
    ball["x"] = ball["x"] + ball["vx"] * dt
    ball["y"] = ball["y"] + ball["vy"] * dt

    if ball["x"] < 0:
        ball["x"] = 0
        ball["vx"] = -ball["vx"]
    if ball["x"] + ball["w"] > WIDTH:
        ball["x"] = WIDTH - ball["w"]
        ball["vx"] = -ball["vx"]
    if ball["y"] < 0:
        ball["y"] = 0
        ball["vy"] = -ball["vy"]


# ---- YOUR BAT BOUNCE GOES HERE -------------------------------
