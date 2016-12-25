import sys

import pygame
from settings import Settings

def run_game():
    # Init game and create a window.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Start main loop of the game.
    while True:
        # Handling events from keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()

run_game()



