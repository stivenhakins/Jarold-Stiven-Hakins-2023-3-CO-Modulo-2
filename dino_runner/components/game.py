import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, HEART

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.menu import Menu
from dino_runner.components.score import Score
from dino_runner.components.message import Message


class Game:
    GAME_SPEED = 20

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu('Press any key to start...', self.screen)
        self.score = Score()
        self.message = Message(self.screen)
        self.death_count = 0
        self.power_up_manager = PowerUpManager()
        self.counter = 10

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset_all()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.score.highest_score()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.score.update_score(self)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw_score(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        if self.obstacle_manager.hearts_life == 1:
            self.draw_hearts_life(self.counter)
        if self.obstacle_manager.hearts_life == 2:
            self.draw_hearts_life(self.counter)
            self.draw_hearts_life(self.counter + 25)
        if self.obstacle_manager.hearts_life == 3:
            self.draw_hearts_life(self.counter)
            self.draw_hearts_life(self.counter + 25)
            self.draw_hearts_life(self.counter + 50)
        pygame.display.update()
        # pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        self.menu.reset_screen_color(self.screen)

        if self.death_count > 0:
            self.menu.update_message("Game Over. Press any key to restart", 0)
            self.message.your_score(self.screen, self.score.total_score())
            self.message.highest_score(self.screen, self.score.highest_score())
            self.message.total_deaths(self.screen, self.death_count)
        self.menu.draw(self.screen)

        self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 150))

        self.menu.update(self)
    
    def reset_all(self):
        self.game_speed = self.GAME_SPEED
        self.obstacle_manager.reset()
        self.score.reset_score()
        self.player.reset()
        self.power_up_manager.reset()
        self.obstacle_manager.hearts_life = 0
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                self.message.time_to_show(self.screen, time_to_show, self.player.type)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
    
    def draw_hearts_life(self, x_postion): 
        image = HEART
        rect = image.get_rect()
        rect.x = x_postion
        rect.y = 10
        self.screen.blit(image, rect)
