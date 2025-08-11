import pygame
import pygame.image
import pygame.display
import pygame.font

class Button:
    """Button class to create various buttons on the screen"""

    def __init__(self, ai_game, msg):
        """Construct a custom button"""
        self.settings = ai_game.settings

        # Screen properties
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
        # Each new button will be placed below the previous one so create an offset
        self.rect.y += self.settings.button_count * (self.height + 10)

        # Turn msg into an image and center it on the button
        self.text = self.font.render(msg, True, self.text_color, self.color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center

        # Keep buttons count to know where the place the next one
        self.settings.button_count += 1

    def draw(self):
        """Draw button and text"""
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.text, self.text_rect)
