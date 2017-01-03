class Settings():
    """ Class for game settings."""

    def __init__(self):
        """ Init game settings."""
        # Parameters
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings.
        self.ship_speed_factor = 20
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings.
        self.alien_speed_factor = 4
        self.fleet_drop_speed = 30
        # fleet_direction = 1 right, -1 left
        self.fleet_direction = 1