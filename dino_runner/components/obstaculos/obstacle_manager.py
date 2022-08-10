import pygame
import random

from dino_runner.components.obstaculos.cactus import Cactus
from dino_runner.components.obstaculos.cactus import Cactus_alto
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
class Obstacle_manager:
    def __init__(self):
        self.obstacles = []
        

    def update(self, game):
        numero = random.randint(0,20)
        if len(self.obstacles) == numero % 2 == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        if len(self.obstacles) == numero % 2 == 1:
            self.obstacles.append(Cactus_alto(LARGE_CACTUS))
                    

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    
    def drawn(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
