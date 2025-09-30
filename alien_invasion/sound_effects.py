import pygame
import pygame.mixer

pygame.mixer.init()

background_sound = pygame.mixer.Sound('sounds/relax_beat.mp3')
bullet_sound = pygame.mixer.Sound('sounds/laser_gun_shot.wav')
death_sound = pygame.mixer.Sound('sounds/system_break_down.wav')
explosion_sound = pygame.mixer.Sound('sounds/explosion.wav')