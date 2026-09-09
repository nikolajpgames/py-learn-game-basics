# Session 6 - Your First Window
#
# Any line starting with a # is a note for humans.
# Python skips them completely, so you can write whatever you like.


import pygame  # bring in the games library

pygame.init()                    # wake pygame up. This always comes first.


# Make the window. The two numbers are its width and height, in pixels.
screen = pygame.display.set_mode((800, 450))

# The words that show up in the window's title bar, at the top.
pygame.display.set_caption("Session 6")

# A clock. Its job is to hold the loop below to a steady speed.
clock = pygame.time.Clock()


# ---- THE GAME LOOP ---------------------------------------------------
# Everything indented below runs over and over, about 60 times a second,
# and keeps running until "running" becomes False.
# One trip round this loop = one frame of your game.
# ----------------------------------------------------------------------

running = True
while running:

    # Windows is constantly sending this program little messages:
    # a key went down, the mouse moved, the X was clicked.
    # We have to collect them every frame, or the window freezes up.
    for event in pygame.event.get():

        if event.type == pygame.QUIT:     # someone clicked the X
            running = False               # so stop going round the loop

    # Paint the whole window one flat colour.
    # The three numbers are RED, GREEN and BLUE, each from 0 to 255.
    screen.fill((20, 22, 34))

    # Everything above was painted onto a hidden page you can't see yet.
    # flip() swaps that page to the front, all in one go.
    # That's why you never catch the picture half-finished.
    pygame.display.flip()

    # Wait just long enough to keep this loop at 60 frames a second.
    # Take this line out and it runs as fast as your computer physically
    # can - about ten thousand times a second - for no benefit at all.
    clock.tick(60)


# The loop has finished, so shut pygame down tidily before we go.
pygame.quit()
