# Arkanoid - everything that draws.

import pygame
from config import *

pygame.font.init()
font = pygame.font.Font(None, TEXT_SIZE)


def draw(screen, bat, ball, bricks, lives, mode):
    screen.fill(BG)

    for brick in bricks:
        pygame.draw.rect(screen, brick["colour"],
                         (brick["x"], brick["y"], brick["w"], brick["h"]))

    pygame.draw.rect(screen, BAT_COLOUR, (bat["x"], bat["y"], bat["w"], bat["h"]))
    pygame.draw.rect(screen, BALL_COLOUR, (ball["x"], ball["y"], ball["w"], ball["h"]))

    img = font.render(f"LIVES {lives}", True, TEXT_COLOUR)
    screen.blit(img, (12, 10))

    if mode == "over":
        img = font.render("GAME OVER - PRESS R", True, TEXT_COLOUR)
        screen.blit(img, (WIDTH / 2 - img.get_width() / 2,
                          HEIGHT / 2 - img.get_height() / 2))
