import pygame

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prepare_score()
        self.prepare_high_score()
        self.prepare_level()

    def prepare_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_string = "{:,}".format(rounded_score)
        score_string = 'SCORE - ' + score_string
        self.score_image = self.font.render(score_string, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 0

    def prepare_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_string = "{:,}".format(high_score)
        high_score_string = 'HI-SCORE - ' + high_score_string
        self.high_score_image = self.font.render(high_score_string, True, self.text_color, self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.centerx = self.screen_rect.centerx

    def prepare_level(self):
        self.level_image = self.font.render('LEVEL - ' + str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.show_lifes()

    def show_lifes(self):
        ship_left_position = 10
        for ship_number in range(self.stats.ships_left):
            self.screen.blit(pygame.image.load('images/mini-ship.png'), [ship_left_position, 5])
            ship_left_position += 30