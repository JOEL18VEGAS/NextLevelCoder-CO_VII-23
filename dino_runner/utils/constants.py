# Third Party Imports
import pygame.gfxdraw
import os

# Global Constants
TITLE = "Next Level Coder CO"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
FPS = 30
GRAVITY = 0.8
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

# Dinosaur Constants.
DINOS_INITIAL_POSITION = [[80, SCREEN_HEIGHT - 100], [200, 500]]

# Background Image.
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/background_dino.gif'))

# Floor Image.
FLOOR_IMG = pygame.image.load(os.path.join(IMG_DIR, "Other/floor_one.png"))

# Controllers.
CONTROLS = (
    # Player 1 wasd
    {
        "jump": pygame.K_w,
        "duck": pygame.K_s,
        "left": pygame.K_a,
        "right": pygame.K_d,
    },
    # Player 2 arrows
    {
        "jump": pygame.K_UP,
        "duck": pygame.K_DOWN,
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
    },
)

# To be removed...
RUNNING = [
    # Player 1
    (pygame.image.load(os.path.join(IMG_DIR, "Dinos/male/vita/base/run_one.png")),
     pygame.image.load(os.path.join(IMG_DIR, "Dinos/male/vita/base/run_two.png")),),
    # Player 2
    (pygame.image.load(os.path.join(IMG_DIR, "Dinos/male/mort/base/run_one.png")),
     pygame.image.load(os.path.join(IMG_DIR, "Dinos/male/mort/base/run_two.png")),)
]  # Remove this...

# Player 1 Assets.
PLAYER_1 = {
    "RUNNING": [
        pygame.image.load(os.path.join(IMG_DIR, "Dinos/male/vita/base/run_one.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dinos/male/vita/base/run_two.png")),
    ],
    "DUCKING": pygame.image.load(os.path.join(IMG_DIR, "Dinos/male/vita/base/duck.png")),
    # "MOVEMENT": {
    #     # "LEFT": pygame.image.load(os.path.join(IMG_DIR, "Dinos/male/vita/base/move_left.png")),
    # }
}

# Obstacles or Enemies Assets.
ENEMIES = {
    "EGGS": [
        pygame.image.load(os.path.join(IMG_DIR, "EggEnemy/egg_one.png")),
        pygame.image.load(os.path.join(IMG_DIR, "EggEnemy/egg_two.png")),
        pygame.image.load(os.path.join(IMG_DIR, "EggEnemy/egg_three.png")),
    ],
    "ASTEROID": [
        pygame.image.load(os.path.join(IMG_DIR, "Asteroid/asteroid_one.png")),
    ],
    "METEORITE": [
        pygame.image.load(os.path.join(IMG_DIR, "Meteorite/meteorite_one.png")),
    ],

}

# Power Ups Assets.
POWER_UPS = {
    "COIN": [
        pygame.image.load(os.path.join(IMG_DIR, "Coin/coin_one.png")),
    ],
    "SHIELD": [
        pygame.image.load(os.path.join(IMG_DIR, "Shield/recoil_shield.png")),
    ],
    "LIVES": [
        pygame.image.load(os.path.join(IMG_DIR, "Heart/heart_filled.png")),
    ],
    "CLOCK": [
        pygame.image.load(os.path.join(IMG_DIR, "Clock/time_increase.png")),
    ],
}

DEFAULT_TYPE = "default"
