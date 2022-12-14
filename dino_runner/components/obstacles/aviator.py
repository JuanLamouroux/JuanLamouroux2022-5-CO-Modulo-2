import random
import pygame
from dino_runner.components.obstacles.obstacles import Obstacle

class Aviator(Obstacle):

    def __init__(self,image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.x = random.randint(1200,2000)
        self.rect.y = random.randint(0,200)
        
        