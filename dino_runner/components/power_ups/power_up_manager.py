import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
number = random.randint(0, 3)
class PowerUpsManager():
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generated_power_up(self, points):
        number = random.randint(0, 3)
        if len(self.power_ups) == 0:
            if self.when_appears == points:
                if number % 2 == 0:
                    self.when_appears = random.randint(self.when_appears + 200, self.when_appears + 300)
                    self.power_ups.append(Shield())
                else:
                    self.when_appears = random.randint(self.when_appears + 200, self.when_appears + 300)
                    self.power_ups.append(Hammer())

    def update(self, points, game_speed, player):
        self.generated_power_up(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                    power_up.start_time = pygame.time.get_ticks()
                    player.shield = True
                    player.hammer = True
                    player.show_text = True
                    player.type = power_up.type
                    time_random = random.randint(5, 8)
                    player.shield_time_up = power_up.start_time + (time_random * 1000)
                    player.hammer_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)