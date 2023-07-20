import random

from dino_runner.components.powerups.powerup import PowerUp
from dino_runner.utils.constants import POWER_UPS

class UpLives(PowerUp):

    def __init__(self):
        # Select a random image from the list of live images.
        selected_image = random.choice(POWER_UPS['LIVES'])
        # Call the constructor of the parent class.
        super().__init__(selected_image)
        # Set the random position of the asteroid.
        self.rect.y = random.randint(150, 400)

    # Update the position of the power up.
    def update(self, game):
        pass


