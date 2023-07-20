# Third party imports.
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


# PowerUp class.
class PowerUp(Sprite):

    # Constructor.
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 100
        self.rect.y = 400

    # Update the power up.
    def update(self, game_speed):

        self.rect.x -= game_speed
        return self.rect.x > 0

    # Draw the power up.
    def draw(self, screen):
        # Draw in the screen.
        screen.blit(self.image, self.rect)

