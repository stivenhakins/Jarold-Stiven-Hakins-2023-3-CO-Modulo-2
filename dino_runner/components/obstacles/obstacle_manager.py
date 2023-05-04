import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE


class ObstacleManager:
  def __init__(self):
    self.obstacles = []
    self.hearts_life = 0
    
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
        if game.player.type == SHIELD_TYPE:
          self.obstacles.remove(obstacle)
        elif game.player.type == HAMMER_TYPE and self.hearts_life < 3:
          self.obstacles.remove(obstacle)
          self.hearts_life += 1
        elif game.player.type == DEFAULT_TYPE and self.hearts_life > 0:
          self.hearts_life -= 1

        if self.hearts_life > 0:
          pass
        else:
          game.playing = False
          pygame.time.delay(1000)
          game.death_count += 1
          break
  
  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)

  def reset(self):
    self.obstacles = []
