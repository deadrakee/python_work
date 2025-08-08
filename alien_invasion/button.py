import pygame
import pygame.image
import pygame.display
import pygame.font

class Button:
    """Button class to create various buttons on the screen"""

    def __init__(self, ai_game, msg):
        """Construct a custom button"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Properties of button and text
        self.width, self.height = 200, 50
        self.color = (0, 135, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Build button rect and center it
        self.rect = pygame.Rect((0,0), (self.width, self.height))
        self.rect.center = self.screen_rect.center

        # Turn msg into an image and center it on the button
        self.text = self.font.render(msg, True, self.text_color, self.color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center


    def draw(self):
        """Draw button and text"""
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.text, self.text_rect)
