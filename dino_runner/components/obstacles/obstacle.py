# Third party imports.
from pygame.sprite import Sprite

# Local imports.
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Obstacle class.
class Obstacle(Sprite):
    # Constructor Method.
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.vertical_position = False

    # Update Method. This method is called automatically by the update() method in the main game loop.
    def update(self, game_speed):

        if self.vertical_position:
            self.rect.y += game_speed
            return self.rect.y < (SCREEN_HEIGHT + self.rect.height)

        else:
            # Move the obstacle to the left.
            self.rect.x -= game_speed
            # Check if the obstacle is no longer visible on the screen.
            return self.rect.x > 0

    # Draw Method. This method is called automatically by the draw() method in the main game loop.
    def draw(self, screen):
        # Draw the image.
        screen.blit(self.image, self.rect)
