import random
import pygame
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.components.dinosaur import Dinosaur


class Aviator(Obstacle):

    def __init__(self,image):
        self.step_aviator = Dinosaur().step_index
        self.type = 0 if self.step_aviator < 5 else 1 
        super().__init__(image, self.type)
        