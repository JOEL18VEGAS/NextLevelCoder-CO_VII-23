# Third party imports.
import random

# Local imports.
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import ENEMIES


# Egg class.
class Egg(Obstacle):
    # Constructor.
    def __init__(self):
        # Select a random image from the list of egg images.
        selected_image = random.choice(ENEMIES['EGGS'])
        # Call the constructor of the parent class.
        super().__init__(selected_image)
        # Set the fix y position of the egg. ( in progress )
        self.rect.y = 400



