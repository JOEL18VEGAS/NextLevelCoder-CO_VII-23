# Floor class.
class Floor:
    # Constructor.
    def __init__(self, image, position):
        self.image = image
        self.position = position

    # Update the floor.
    def draw(self, screen, game_speed):
        # Get the width of the image.
        image_width = self.image.get_width()

        # Draw the image.
        screen.blit(self.image, self.position)

        # Draw the image behind the first image.
        screen.blit(self.image, (image_width + self.position[0], self.position[1]))

        # If the image is off the screen almost one pixel, draw it behind the first image.
        if self.position[0] <= -image_width:
            screen.blit(self.image, (image_width + self.position[0], self.position[1]))
            self.position[0] = 0

        # Move the image to the left.
        self.position[0] -= game_speed
