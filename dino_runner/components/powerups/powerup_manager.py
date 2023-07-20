# Third party imports.
import random

from .shield import Shield
# Local imports.
from .uplives import UpLives
from .upscore import UpScore
from .velocity_reducer import VelocityReducer


# PowerUpManager class.
class PowerUpManager:
    # Constructor.
    def __init__(self):
        self.power_up = None
        self.has_power_up = False

    # Update the obstacles.
    def update(self, game ):
        # If doesn't have an obstacle, add one.
        if not self.has_power_up:
            # Add an obstacle.
            self.add_powerup()
        # has_obstacle is True if obstacle.update() returns True.
        self.has_power_up = self.power_up.update(game.game_speed)

        # If the player collides with the obstacle, the game ends.
        if game.players[0].rect.colliderect(self.power_up.rect):
            print("Collision")
            game.playing = False

    # Draw the obstacles.
    def draw(self, screen):
        # If it has an obstacle, draw it.
        if self.has_power_up:
            # Draw the obstacle.
            self.power_up.draw(screen)

    # Add an obstacle.
    def add_powerup(self):
        # Add an obstacle.
        self.power_up = random.choice((UpLives(), VelocityReducer(), UpScore(), Shield() ))
        # has_obstacle is True.
        self.has_power_up = True
