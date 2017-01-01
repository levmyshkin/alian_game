class Settings():
    """ Class for game settings."""

    def __init__(self):
        """ Init game settings."""
        # Parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 20
        # Bullet settings.
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3