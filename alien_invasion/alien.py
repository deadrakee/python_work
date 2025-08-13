import pygame
import pygame.image
import pygame.sprite

class Alien(pygame.sprite.Sprite):
    """Contains characteristics of a single alien"""

    def __init__(self, ai_game):
        """Create new sprite almost in the top left corner"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen(one alien spacing)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Store its row and column postion
        self.row = 0
        self.col = 0

    def check_edges(self):
        """Return True if an alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.left <= 0) or (self.rect.right >= screen_rect.right)

    def update(self):
        """Move the alien left and right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x