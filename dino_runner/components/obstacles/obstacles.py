import pygame

from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH, BIRD


class Obstacle(Sprite):

    def __init__(self,image, obstacle_type):
        self.image = image
        self.obstacle_type = obstacle_type
        self.rect = self.image[self.obstacle_type].get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < - self.rect.width:
            obstacles.pop()

 
    def draw(self,screen):
        screen.blit(self.image[self.obstacle_type], (self.rect.x, self.rect.y))

'''class Aviator(Sprite):

    def __init__(self,image):
        self.image = image
        self.fly_rect = self.image.get_rect()
        self.fly_rect.x = SCREEN_WIDTH
        self.dino_rect.y
        self.fly_index = 0
        
    def update(self, game_speed, flys):
        self.fly_rect.x -= game_speed

        if self.fly_rect.x < - self.fly_rect.width:
            flys.pop()

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.fly_rect.x
        self.dino_rect.y = self.dino_rect.y
        self.fly_index += 0
 
    def draw(self,screen):
        screen.blit(self.image, (self.fly_rect.x, self.fly_rect.y))      '''

    