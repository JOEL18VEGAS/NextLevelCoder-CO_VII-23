
# Platform class. This class is used to create the platforms in the future.
class Platform:
    # Constructor.
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]