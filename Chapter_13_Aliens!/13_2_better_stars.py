### 13-1. Stars:

import pygame
import pygame.display
import pygame.image
import pygame.sprite
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    """The star class"""

    def __init__(self):
        """Create a single star sprite"""
        super().__init__()
        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


#screen
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
screen_rect = screen.get_rect()

#star group and size
stars = pygame.sprite.Group()
dummy_star = Star()
star_width, star_height = dummy_star.rect.size

#creating the sky
current_x = star_width
current_y = star_height

while current_y < (screen_rect.height - 2*star_height):
    while current_x < (screen_rect.width - 2*star_width):
        new_star = Star()
        random_number = randint(-40, 40)
        new_star.rect.x = current_x+random_number
        new_star.rect.y = current_y+random_number
        stars.add(new_star)
        current_x += 2*star_width
    current_x = star_width
    current_y += 2*star_height

while True:
    stars.draw(screen)
    pygame.display.flip()