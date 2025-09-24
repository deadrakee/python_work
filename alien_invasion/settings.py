"""Module containing settings"""
import random

# Colors
TRANSPARENT = (0, 0, 0, 0)

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settigns
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.fullscreen = False
        self.button_count = 0

        # Ship settings
        self.ship_limit = 3
        self.ship_width = 60
        self.ship_height = 48

        # Bullet settings
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
        self.bullet_invincible = False

        # Enemy bullets
        self.enemy_bullet_color = (0, 135, 0)
        self.enemy_bullet_speed = 2
        self.enemy_bullet_width = 3
        self.eb_spawn_cd = 100

        # Alien settings
        self.fleet_drop_speed = 10

        # Shield size
        self.shield_shape = "image"
        self.shield_count = 3
        self.shield_width = 100
        self.shield_height = 30
        self.shield_bottom = self.screen_height-200
        self.shield_color = (0, 100, 0, 255)
        self.dent_radius_multi = 2.8

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # Kill points ramping scale
        self.score_scale = 1.5

        self.init_dynamic_settings()


    def init_dynamic_settings(self):
        """Settings which will reset at runtime"""
        self.alien_speed = 1.0 
        self.ship_speed = 3
        self.bullet_speed = 4
        self.bullet_width = 3
        self.alien_points = 50

        # Move right: 1; Move left: -1
        self.fleet_direction = 1


    def _speedup_game(self):
        """Changes settings after wave clear"""
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        # Make aliens more rewarding each new level
        self.alien_points = int(self.alien_points * self.score_scale)


    def init_easy_settings(self):
        """Make the ship and bullets fast"""
        self.ship_speed = 6
        self.bullet_speed = 6
        self.bullet_width = 3000


    def init_hard_settings(self):
        """Make the aliens fast"""
        self.alien_speed = 6.0 


    def change_bg_color_randomly(self):
        """Changes the background with a random color"""
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.bg_color = (r, g, b)