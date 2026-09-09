# Arkanoid - everything that draws.

import pygame
from config import *


def draw(screen, bat, ball, bricks):
    screen.fill(BG)

    for brick in bricks:
        pygame.draw.rect(screen, brick["colour"],
                         (brick["x"], brick["y"], brick["w"], brick["h"]))

    pygame.draw.rect(screen, BAT_COLOUR, (bat["x"], bat["y"], bat["w"], bat["h"]))
    pygame.draw.rect(screen, BALL_COLOUR, (ball["x"], ball["y"], ball["w"], ball["h"]))
