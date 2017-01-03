import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # Init game and create a window.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, 'Play')
    stats = GameStats(ai_settings)
    # Creating a ship.
    ship = Ship(ai_settings, screen)
    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.flip()

    # Start main loop of the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        else:
            if stats.ships_left > 0:
                play_button.draw_button()
                gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
            # else:
            #     game_over_image = pygame.image.load('images/game_over.png')
            #     game_over_rect = pygame.Rect(screen.get_rect().centerx - 150, screen.get_rect().centery - 150, 300, 300)
            #     screen.blit(game_over_image, game_over_rect)
            #     pygame.display.flip()


run_game()



