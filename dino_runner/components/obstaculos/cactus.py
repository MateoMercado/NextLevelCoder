import random

from dino_runner.components.obstaculos.obstaculo import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint( 0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325
        
class Cactus_alto(Obstacle):
    def __init__(self, image):
        self.type = random.randint( 0, 2)
        super().__init__(image, self.type)
        self.rect.y = 305
class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 205
        self.index = 0