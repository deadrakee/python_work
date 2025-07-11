"""Module containing settings"""
import random
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settigns
        self.scree_width = 1200
        self.scree_height = 800
        self.bg_color = (230, 230, 230)
        self.fullscreen = False

        # Ship settings
        self.ship_speed = 2.5

    def change_bg_color_randomly(self):
        """Changes the background with a random color"""
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.bg_color = (r, g, b)