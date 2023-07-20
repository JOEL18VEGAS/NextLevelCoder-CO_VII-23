# Third party imports.
import random

# Local imports.
from .powerup import PowerUp
from ...utils.constants import POWER_UPS


# VelocityReducer class.
class VelocityReducer(PowerUp):

    # Constructor.
    def __init__(self):
        # Select a random image from the list of meteorite images.
        selected_image = random.choice(POWER_UPS['CLOCK'])
        # Set the random position of the meteorite.
        # Call the constructor of the parent class.
        super().__init__(selected_image)
        # Set the random position of the asteroid.
        self.rect.y = 440
