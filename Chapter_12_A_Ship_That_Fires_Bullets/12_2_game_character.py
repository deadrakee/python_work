### 12-2. Game Character: 

import pygame
import pygame.display
import pygame.image

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
screen.fill((0, 0, 230))

image = pygame.image.load('batman_pixel_art.png')
image_rect = image.get_rect()
image_rect.center = screen.get_rect().center

screen.blit(image, image_rect)
pygame.display.flip()

while True:
    None