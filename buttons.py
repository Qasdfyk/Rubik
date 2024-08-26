import pygame
from pygame.locals import *

pygame.init()
font = pygame.font.Font(None, 36)
button_width = 120
button_height = 50
button_x = 800 - button_width - 10 
button_y = 600 - button_height - 10

class ShuffleButton:
    def __init__(self, x=button_x, y=button_y, width=button_width, height=button_height, text="Shuffle", font=font, bg_color=(160, 160, 160), text_color=(0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


class SolveButton:
    def __init__(self, x=button_x, y=(button_y-70), width=button_width, height=button_height, text="Solve", font=font, bg_color=(160, 160, 160), text_color=(0,0,0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)