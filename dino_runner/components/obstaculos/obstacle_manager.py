import pygame
import random

from dino_runner.components.obstaculos.cactus import Cactus
from dino_runner.components.obstaculos.cactus import Cactus_alto
from dino_runner.components.obstaculos.cactus import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
class Obstacle_manager:
    def __init__(self):
        self.obstacles = []
        

    def update(self, game):
        numero = random.randint(0,2)
        if numero == 0:
            if len(self.obstacles) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        if numero == 1:           
            if len(self.obstacles) == 0:
                self.obstacles.append(Cactus_alto(LARGE_CACTUS))
        if numero == 2:           
            if len(self.obstacles) == 0:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                else:
                    self.obstacles.remove(obstacle)
                break
    
    def drawn(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
