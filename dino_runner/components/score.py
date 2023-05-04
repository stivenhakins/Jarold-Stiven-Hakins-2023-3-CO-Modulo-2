import pygame

from dino_runner.utils.constants import FONT_STYLE


class Score():
    def __init__(self):
        self.score = 0
        self.highest = 0

    def update_score(self, game):
        self.score += 1

        if self.score % 100 and game.game_speed < 250 == 0:
            game.game_speed += 5


    def draw_score(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        screen.blit(text, text_rect)
    
    def reset_score(self):
        self.score = 0
    
    def highest_score(self):
        if self.score > self.highest:
            self.highest = self.score
        return self.highest

    def total_score(self):
        return self.score
