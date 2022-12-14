import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.aviator import Aviator

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.ramdon = random.randint(0,3)

        if len(self.obstacles) == 0 and self.ramdon == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)
            
        elif len(self.obstacles) == 0 and self.ramdon == 1:
            cactus = Cactus(LARGE_CACTUS)
            self.obstacles.append(cactus)
        

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
