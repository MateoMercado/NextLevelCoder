from asyncio import shield
from email.mime import image
from dino_runner.utils.constants import SHIELD_TYPE, SHIELD
from dino_runner.components.power_ups.power_up import PowerUp

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)