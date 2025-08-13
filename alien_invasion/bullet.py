import pygame
import pygame.display
import pygame.draw
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at a ships position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings    

    def update(self):
        """Move a bullet up the screen"""
        self.y += self.bullet_speed*self.direction
        self.rect.y = self.y

    def draw_bullet(self):
        """Place a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class ShipBullet(Bullet):
    """Initiated by the ship"""

    def __init__(self, ai_game, shooter_rect):
        super().__init__(ai_game)
        self.color = self.settings.bullet_color
        self.bullet_speed = self.settings.bullet_speed

        # Move up the screen
        self.direction = -1

        # create a bullet rect at (0, 0) and then move to ship position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = shooter_rect.midtop

        # Store the bullet's position as a float
        self.y = float(self.rect.y)


class AlienBullet(Bullet):
    """Initiated by an alien"""

    def __init__(self, ai_game, shooter_rect):
        super().__init__(ai_game)
        self.color = self.settings.enemy_bullet_color
        self.bullet_speed = self.settings.enemy_bullet_speed

        # Move down the screen
        self.direction = 1

        # Create a bullet rect at (0, 0) with specific size
        self.rect = pygame.Rect(0, 0, self.settings.enemy_bullet_width,
                                self.settings.bullet_height)
        
        # Move to alien position
        self.rect.midbottom = shooter_rect.midbottom

        # Store the bullet's position as a float
        self.y = float(self.rect.y)