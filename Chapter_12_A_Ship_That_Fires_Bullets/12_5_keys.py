### 12-5. Keys:

import pygame
import pygame.display
import pygame.event

pygame.init()
screen = pygame.display.set_mode((1920, 1080))

while True:
    None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.unicode)