import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' Class for alien ships. '''

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien-ship.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        ''' Display image. '''
        self.screen.blit(self.image, self.rect)