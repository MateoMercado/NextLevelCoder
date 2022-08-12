import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_COLOR = (0, 0, 0,)
FONT_SIZE = 30
FONT_STYLE = 'freesansbold.ttf'

def Message(
        message,
        screen, 
        font_color = FONT_COLOR,
        font_size = FONT_SIZE,
        posYcenter = SCREEN_HEIGHT // 2,
        posXcenter = SCREEN_WIDTH // 2
    ):
     
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(message, True, font_color)
        text_rect = text.get_rect()
        text_rect.center = (posXcenter, posYcenter)
        screen.blit(text, text_rect)