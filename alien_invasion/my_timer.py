# Create timer API

import pygame
import pygame.time

class Timer():
    """The timer class"""

    def __init__(self, duration):
        """Construct with given duration, the rest is default"""
        self.duration = duration #ms
        self.start_time = 0
        self.passed = 0
        self.running = False


    def start_timer(self, duration=None):
        """Store starting time, clear previous and raise flag. 
        If no duration is given, use the current self.duration"""
        if duration is not None:
            self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.passed = 0
        self.running = True


    def is_elapsed(self):
        """Return if elapsed time is larger then duration"""
        if self.running:
            current_time = pygame.time.get_ticks()
            passed = self.passed + (current_time - self.start_time)
            return passed > self.duration
        

    def suspend(self):
        """Store the elapsed time so far and lower flag"""
        current_time = pygame.time.get_ticks()
        self.passed += current_time - self.start_time
        self.running = False


    def resume(self):
        """Renew starting point and raise flag"""
        self.start_time = pygame.time.get_ticks()
        self.running = True


    def get_elapsed(self):
        """Return how much time passed"""
        if self.running:
            current_time = pygame.time.get_ticks()
            return self.passed + (current_time - self.start_time)
        else:
            return self.passed