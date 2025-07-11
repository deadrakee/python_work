import pygame

def mutate_a(a):
    """change a"""
    a += 30

def mutate_x(rect_obj):
    """modify rect in method"""
    rect_obj.x = 10

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
rect_obj = screen.get_rect()
print(f"before: {rect_obj.x}")

mutate_x(rect_obj)
print(f"after: {rect_obj.x}")


a = 2
print(a)
mutate_a(a)
print(a)