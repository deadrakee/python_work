import pygame
import pygame.image

from direction import MoveRight, MoveLeft

class Ship:
    """Create and manipulate a ship, representing a player"""

    def __init__(self, ai_game):
        """Init the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship's image and get its rect.
        self.image = pygame.image.load('images/ship.bmp') 
        self.rect = self.image.get_rect()

        # Place ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement by key pressing
        self.r_direction = MoveRight(self.rect)
        self.l_direction = MoveLeft(self.rect)

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def move(self):
        """Move in all active directions"""
        self.x = self.r_direction.move(self.settings.ship_speed, self.x)
        self.x = self.l_direction.move(self.settings.ship_speed, self.x)
