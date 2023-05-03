import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
  def __init__(self):
    self.obstacles = []
    
  def generate_obstacle(self, obstacle_type):
    if obstacle_type == 0:
      cactus_type = 'SMALL'
      obstacle = Cactus(cactus_type)
    elif obstacle_type == 1:
      cactus_type = 'LARGE'
      obstacle = Cactus(cactus_type)
    else:
      obstacle = Bird()
    return obstacle
    
  def update(self, game):
    if len(self.obstacles) == 0:
      obstacle_type = random.randint(0, 2)
      obstacle = self.generate_obstacle(obstacle_type)
      self.obstacles.append(obstacle)
    
    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      if game.player.dino_rect.colliderect(obstacle.rect):
        game.playing = False
        pygame.time.delay(1000)
        break
  
  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)
