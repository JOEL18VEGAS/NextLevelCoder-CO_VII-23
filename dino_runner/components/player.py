# Local imports
from .dinosaur import Dinosaur


# Player class.
class Player(Dinosaur):
    # Constructor.
    def __init__(self, screen, position, images):
        super().__init__(screen=screen, position=position, images=images)
        self.score = 0
        self.is_alive = True
        self.name = 'player1'
        self.images = images

    # Get the score of the player.
    def get_score(self):
        return self.score

    # Set the score of the player.
    def set_score(self, score):
        self.score = score
        return self.score

    # Get the status of the player.
    def get_status(self):
        return self.is_alive

    # Set the status of the player.
    def set_status(self, status):
        self.is_alive = status
        return self.is_alive

    # Get the name of the player.
    def get_name(self):
        return self.name

    # Set the name of the player.
    def set_name(self, number):
        self.name = 'player' + str(number)
        return self.name
