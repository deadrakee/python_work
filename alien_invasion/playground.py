import pygame
import pygame.draw

def mutate_a(a):
    """change a"""
    a += 30

def mutate_x(rect_obj):
    """modify rect in method"""
    rect_obj.x = 10

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

bullet_rect = pygame.Rect(0, 0, 2, 15)
bullet_rect.center = screen_rect.center
pygame.draw.rect(screen, (0,0,255), bullet_rect)
pygame.display.flip()

while True:
    None