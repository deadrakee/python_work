import pygame
import pygame.image
import pygame.sprite

class Alien(pygame.sprite.Sprite):
    """Contains characteristics of a single alien"""

    def __init__(self, ai_game):
        """Create new sprite almost in the top left corner"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen(one alien spacing)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)