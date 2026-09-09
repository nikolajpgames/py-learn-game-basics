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


def overlaps(a, b):
    if a["x"] + a["w"] < b["x"]:
        return False
    if b["x"] + b["w"] < a["x"]:
        return False
    if a["y"] + a["h"] < b["y"]:
        return False
    if b["y"] + b["h"] < a["y"]:
        return False
    return True


def bounce_off_bat(ball, bat):
    # only when the ball is actually heading downwards, or it sticks
    if ball["vy"] < 0:
        return

    if not overlaps(ball, bat):
        return

    ball["y"] = bat["y"] - ball["h"]
    ball["vy"] = -ball["vy"]

    # where along the bat did it land? -1 at the far left, 1 at the far right
    hit = (ball["x"] + ball["w"] / 2) - (bat["x"] + bat["w"] / 2)
    ball["vx"] = (hit / (bat["w"] / 2)) * BALL_SPEED


def make_bricks():
    bricks = []
    left = (WIDTH - (BRICK_COLS * (BRICK_W + BRICK_GAP) - BRICK_GAP)) / 2

    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            brick = {
                "x": left + col * (BRICK_W + BRICK_GAP),
                "y": BRICK_TOP + row * (BRICK_H + BRICK_GAP),
                "w": BRICK_W,
                "h": BRICK_H,
                "colour": BRICK_COLOURS[row % len(BRICK_COLOURS)],
            }
            bricks.append(brick)

    return bricks
