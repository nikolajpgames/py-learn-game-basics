# Arkanoid - everything that draws.

import pygame
from config import *


def draw(screen, bat):
    screen.fill(BG)

    pygame.draw.rect(screen, BAT_COLOUR, (bat["x"], bat["y"], bat["w"], bat["h"]))
