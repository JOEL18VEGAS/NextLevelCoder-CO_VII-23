# Third party imports.
import random

# Local imports.
from ...utils.constants import ENEMIES
from .obstacle import Obstacle

# Asteroid class.
class Asteroid(Obstacle):

    # Constructor.
    def __init__(self):
        # Select a random image from the list of asteroid images.
        selected_image = random.choice(ENEMIES['ASTEROID'])
        # Call the constructor of the parent class.
        super().__init__(selected_image)
        # Set the random position of the asteroid.
        self.rect.x = random.randint(100, 900)
        # Set the y position of the meteorite up the screen.
        self.rect.y = -self.rect.height
        # Set the vertical position of the asteroid.
        self.vertical_position = True
