# Third party imports.
import pygame

# Local imports.
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, PLAYER_1, FPS, FLOOR_IMG, \
    DINOS_INITIAL_POSITION
from .obstacles.obstacles_manager import ObstaclesManager
from .powerups.powerup_manager import PowerUpManager
from .platforms.floor import Floor
from ..utils import constants
from .player import Player


# Game class.
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.players = []
        self.playing = False
        self.game_speed = 8
        self.pos_bg = [0, -30]
        self.floor = Floor(constants.FLOOR_IMG, [0, (SCREEN_HEIGHT - FLOOR_IMG.get_height())])
        self.obstacle_manager = ObstaclesManager()
        self.power_up_manager = PowerUpManager()

    def run(self, players=1):
        self.playing = True
        # If 2 players, create 2 players.
        if (players == 2):
            self.players.append(Player(self.screen, DINOS_INITIAL_POSITION[0], PLAYER_1))
            self.players.append(Player(self.screen, DINOS_INITIAL_POSITION[1], PLAYER_1))
        else:
            self.players.append(Player(self.screen, DINOS_INITIAL_POSITION[0], PLAYER_1))

        while self.playing:
            self.events()
            self.update()
            self.draw()

        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    self.players[0].left()
                if event.key == pygame.K_d:
                    self.players[0].right()

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_a:
                    self.players[0].velocity_x = 0
                if event.key == pygame.K_d:
                    self.players[0].velocity_x = 0

    def update(self):

        if (len(self.players) == 2):
            # first player
            self.players[0].update(pygame.key.get_pressed())
            # second player
            self.players[1].update(pygame.key.get_pressed())

            self.obstacle_manager.update(self)
            self.power_up_manager.update(self)

        # Update the player.
        self.obstacle_manager.update(self)
        self.players[0].update(pygame.key.get_pressed())
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        # Draw the floor.
        self.floor.draw(self.screen, self.game_speed)

        if (len(self.players) == 2):
            # first player
            self.players[0].draw()
            # second player
            self.players[1].draw()

        else:
            self.players[0].draw()
            self.obstacle_manager.draw(self.screen)
            self.power_up_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, self.pos_bg)
        self.screen.blit(BG, (image_width + self.pos_bg[0], self.pos_bg[1]))
        if self.pos_bg[0] <= -image_width:
            self.screen.blit(BG, (image_width + self.pos_bg[0], self.pos_bg[1]))
            self.pos_bg[0] = 0
        self.pos_bg[0] -= self.game_speed
