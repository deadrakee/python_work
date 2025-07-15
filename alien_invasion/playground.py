import pygame
import pygame.draw
import pygame.image
import pygame.sprite

class Alien(pygame.sprite.Sprite):
    """Contains characteristics of a single alien"""

    def __init__(self, ai_game):
        super().__init__()
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

def mutate_a(a):
    """change a"""
    a += 30

def mutate_x(rect_obj):
    """modify rect in method"""
    rect_obj.x = 10

# screen
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
screen_rect = screen.get_rect()
screen.fill((255,255,255))
print(f"before: {screen_rect.x}")

mutate_x(screen_rect)
print(f"after: {screen_rect.x}")

a = 2
print(a)
mutate_a(a)
print(a)

# bullet
bullet_rect = pygame.Rect(0, 0, 2, 15)
bullet_rect.center = screen_rect.center
pygame.draw.rect(screen, (0,0,255), bullet_rect)

# alien
alien_1 = Alien(a)
print(alien_1.image)
print(alien_1.rect)
screen.blit(alien_1.image, alien_1.rect)

while True:
    pygame.display.flip()
    