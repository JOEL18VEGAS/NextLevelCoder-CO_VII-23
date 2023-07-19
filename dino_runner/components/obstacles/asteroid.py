# Local imports.
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH


# Asteroid class. ( in progress )
class Asteroid(Obstacle):

    # Constructor.
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    # Update Method. This method is called automatically by the update() method in the main game loop.
    def update(self):
        pass

    # Draw Method. This method is called automatically by the draw() method in the main game loop.
    def draw(self, screen):
        pass

    # Collision Method. This method is called when the dinosaur collides with an obstacle.
    def collide(self, dinosaur):
        pass