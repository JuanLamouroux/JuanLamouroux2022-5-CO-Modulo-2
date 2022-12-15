import random

from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.utils.constants import BIRD


class Aviator(Obstacle):
  AVIATOR_HEIGHTS = [270, 220, 170]
  def __init__(self):
    self.type = 0
    super().__init__(BIRD, self.type)
    self.rect.y = self.AVIATOR_HEIGHTS[random.randint(0, 2)]
    self.index = 0
    
  def draw(self, screen):
    if self.index >= 9:
     self.index = 0
     
    screen.blit(BIRD[self.index // 5], self.rect)
    self.index += 1
        
        