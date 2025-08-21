import pygame
import pygame.draw

from pygame import Surface
import pygame.mask
from pygame.sprite import Sprite

class Shield(Sprite):
    """A destructable shield sprite"""

    def __init__(self, ai_game):
        """"Create a shield with default params"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Choose shield shape
        if self.settings.shield_shape == "rectangle":
            self._create_rects()
        else:
            self._load_image()

        self.rect = self.image.get_rect()
        
        # place them on a fixed distance from the bottom of the screen
        self.rect.y = self.settings.shield_bottom

        # mask
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_image = self.mask.to_surface()


    def _create_rects(self):
        """Shields are colorfull rectangle in plain surface"""
        self.image = Surface((self.settings.shield_width,self.settings.shield_height), pygame.SRCALPHA)
        self.image.fill(self.settings.shield_color)

    
    def _load_image(self):
        """Shields are in special shape, loaded  by image"""
        self.image = pygame.image.load('images/shield.png')