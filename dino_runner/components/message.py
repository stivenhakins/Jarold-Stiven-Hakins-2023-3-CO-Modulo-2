import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Message:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 22)

    def your_score(self, screen, score):
        text = self.font.render(f'your Score: {score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 40)
        screen.blit(text, text_rect)
    
    def highest_score(self, screen, highest):
        text = self.font.render(f'Highest Score: {highest}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 80)
        screen.blit(text, text_rect)
    
    def total_deaths(self, screen, deaths):
        text = self.font.render(f'Total deaths: {deaths}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 120)
        screen.blit(text, text_rect)
