### 12-4. Rocket:

import sys
import pygame
import pygame.display
import pygame.event
import pygame.image

class Keys:
    """Container for all keypresses"""

    def __init__(self):
        """Build all keys unpressed initially"""
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False


def check_events(keys):
    """Monitors for all events"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_keydown_event(event, keys)
        elif event.type == pygame.KEYUP:
            handle_keyup_event(event, keys)

def handle_keydown_event(event, keys):
    """Handles keypress"""
    if event.key == pygame.K_LEFT:
        keys.left_pressed = True
    elif event.key == pygame.K_RIGHT:
        keys.right_pressed = True
    elif event.key == pygame.K_UP:
        keys.up_pressed = True
    elif event.key == pygame.K_DOWN:
        keys.down_pressed = True
    elif event.key == pygame.K_q:
        sys.exit()
    print(f"KeyDown - {event.key}")

def handle_keyup_event(event, keys):
    """Handles release of a key"""
    if event.key == pygame.K_LEFT:
        keys.left_pressed = False
    elif event.key == pygame.K_RIGHT:
        keys.right_pressed = False
    elif event.key == pygame.K_UP:
        keys.up_pressed = False
    elif event.key == pygame.K_DOWN:
        keys.down_pressed = False
    print(f"KeyUp - {event.key}")

def move_rocket(keys, rocket_rect, screen_rect, speed):
    """move rocket depending on pressed key"""
    if keys.left_pressed and rocket_rect.left > 0:
        rocket_rect.x -= speed
    if keys.right_pressed and rocket_rect.right < screen_rect.right:
        rocket_rect.x += speed
    if keys.up_pressed and rocket_rect.top > 0:
        rocket_rect.y -= speed
    if keys.down_pressed and rocket_rect.bottom < screen_rect.bottom:
        rocket_rect.y += speed


# setup screen
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_rect = screen.get_rect()

#setup keypresses
keys = Keys()

# setup rocket
rocket_surface = pygame.image.load('bat_rocket.png')
rocket_rect = rocket_surface.get_rect()
rocket_rect.center = screen.get_rect().center

while True:
    check_events(keys)
    move_rocket(keys, rocket_rect, screen_rect, 4)
    screen.fill((230, 230, 230))
    screen.blit(rocket_surface, rocket_rect)
    pygame.display.flip()