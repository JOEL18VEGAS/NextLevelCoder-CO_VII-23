import random

from ...utils.constants import POWER_UPS
from .powerup import PowerUp


# UpScore class.
class UpScore(PowerUp):

    # Constructor.
    def __init__(self):
        # Select a random image from the list of coin images.
        selected_image = random.choice(POWER_UPS['COIN'])
        # Call the constructor of the parent class.
        super().__init__(selected_image)
        # Set the random position of the coin.
        self.rect.y = random.randint(150, 400)
