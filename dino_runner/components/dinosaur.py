# Third party imports.
import pygame
from pygame.sprite import Sprite

# Local imports.
import dino_runner.utils.constants as constants

# Dinosaur class.
class Dinosaur(Sprite):
    # Constructor.
    def __init__(self, screen, position, images):
        super().__init__()
        self.images = images
        self.image = self.images["RUNNING"][0]
        self.position = [position[0], 800]
        self.on_ground = True
        self.ducking = False
        self.ducking_pos = 630
        self.running = True
        self.left_direction = False
        self.right_direction = False
        self.velocity_y = 0
        self.velocity_x = 0
        self.step_index = 0
        self.gravity = 1
        self.max_jumps = 2
        self.jumps_left = self.max_jumps
        self.screen = screen

    # Update the dinosaur.
    def update(self, user_input):
        # If the user presses the W key and the dinosaur is on the ground or has jumps left, jump.
        if user_input[pygame.K_w] and (self.on_ground or (not self.on_ground and self.jumps_left > 0)): # The double jump is in progress.
            self.jump()

        # If the user presses the S key, duck.
        elif user_input[pygame.K_s]:
            self.duck()

        # If the user presses the A key, move left.
        elif user_input[pygame.K_a]:
            self.left_direction = True
            self.right_direction = False
            self.left()

        # If the user presses the D key, move right.
        elif user_input[pygame.K_d]:
            self.right_direction = True
            self.left_direction = False
            self.right()

        # If the user doesn't press any key, always run.
        else:
            self.run()

        # Update the position based on the velocity.
        self.position[1] += self.velocity_y

        # Apply gravity to the dinosaur even when ducking in the air.
        if not self.on_ground and self.ducking:
            self.velocity_y += self.gravity

        # Check if the dinosaur has landed on the ground.
        if self.position[1] >= constants.DINOS_INITIAL_POSITION[1][1]:
            self.position[1] = constants.DINOS_INITIAL_POSITION[1][1]
            self.velocity_y = 0
            self.on_ground = True
            self.jumps_left = self.max_jumps

        # Restrict the dinosaur's position within the screen boundaries.
        self.position[0] = max(0, self.position[0])  # Left boundary
        self.position[0] = min(constants.SCREEN_WIDTH - self.image.get_width(), self.position[0])  # Right boundary

        # Reset the step_index when it exceeds the number of images used for running animation.
        if self.step_index >= 10:
            self.step_index = 0

    # Draw the dinosaur to the screen.
    def draw(self):
        # Draw on the screen based on the dinosaur's position.
        self.screen.blit(self.image, [self.position[0], self.position[1] - self.image.get_height()])

    # Jump the dinosaur.
    def jump(self):
        # If the dinosaur is on the ground or has jumps left, perform a jump.
        if self.on_ground or (not self.on_ground and self.jumps_left > 0):
            # Set velocity to a negative value to move the dinosaur up.
            self.velocity_y = -15
            # Set the on_ground flag to False.
            self.on_ground = False
            # Decrease the number of jumps left. ( In Progress )
            self.jumps_left -= 1

    # Duck the dinosaur.
    def duck(self):
        # Set the image to the ducking image.
        self.image = self.images["DUCKING"]
        # Set the ducking flag to True.
        self.ducking = True
        # Set the dinosaur's position to the ducking position.
        self.position[1] = self.position[1] + self.image.get_height()

    # Move the dinosaur to the left.
    def left(self):
        # If the dinosaur is moving right.
        if self.left_direction:
            # Move the dinosaur to the left.
            self.position[0] -= self.velocity_x * 4
            # Increase the velocity.
            self.velocity_x += 0.5

    # Move the dinosaur to the right.
    def right(self):
        # If the dinosaur is moving left.
        if self.right_direction:
            # Move the dinosaur to the right.
            self.position[0] += self.velocity_x * 4
            # Increase the velocity.
            self.velocity_x += 0.5

    # Dinosaur running animation.
    def run(self):
        # Check if the step index is less than the number of images used for running animation.
        self.image = self.images["RUNNING"][0] if self.step_index < 5 else self.images["RUNNING"][1]
        self.step_index += 1
