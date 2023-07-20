# Third party imports.
import random

# Local imports.
from ...utils.constants import ENEMIES
from .obstacle import Obstacle


# Asteroid class.
class Meteorite(Obstacle):

    # Constructor.
    def __init__(self):
        # Select a random image from the list of meteorite images.
        selected_image = random.choice(ENEMIES['METEORITE'])
        # Set the random position of the meteorite.
        # Call the constructor of the parent class.
        super().__init__(selected_image)
        # Set the random position of the asteroid.
        self.rect.y = random.randint(250, 400)
