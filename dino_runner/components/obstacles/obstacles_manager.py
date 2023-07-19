# Local imports.
from dino_runner.components.obstacles.egg import Egg


# Obstacles Manager class.
class ObstaclesManager:
    # Constructor.
    def __init__(self):
        self.obstacle = None
        self.has_obstacle = False

    # Update the obstacles.
    def update(self, game):
        # If doesn't have an obstacle, add one.
        if not self.has_obstacle:
            # Add an obstacle.
            self.add_obstacle()
        # has_obstacle is True if obstacle.update() returns True.
        self.has_obstacle = self.obstacle.update(game.game_speed)

    # Draw the obstacles.
    def draw(self, screen):
        # If has an obstacle, draw it.
        if self.has_obstacle:
            # Draw the obstacle.
            self.obstacle.draw(screen)

    # Add an obstacle.
    def add_obstacle(self):
        # Add an obstacle.
        self.obstacle = Egg()
        # has_obstacle is True.
        self.has_obstacle = True
