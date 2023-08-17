import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 40
BIRD_Y_POS = 260
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

# Dino
DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))
DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))

# Run
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "goku/59.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/60.png")),
]
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "goku/run1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/run2.png")),
]
RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Run/DinoRunHammer2.png")),
]

# Duck
DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "goku/agachar (1).png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/agachar (2).png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/agachar (3).png")),
]
DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "goku/agachar1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/agachar2.png")),
]
DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Duck/DinoDuckHammer2.png")),
]

# Jump
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "goku/pular.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "goku/pulo1.png")
)
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/Jump/DinoJumpHammer.png")
)

# Obstacles
SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "goku/small1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/small2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/small1.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "goku/black.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/jiremlarger.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/beeruslarger.png")),
]
BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "goku/fly_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/fly_2.png")),
]

# Doodads
CLOUD = pygame.image.load(os.path.join(IMG_DIR, "Other/Cloud.png"))

# Power ups
SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Other/Shield.png"))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Other/Hammer.png"))

BG = pygame.image.load(os.path.join(IMG_DIR, "goku/nuvem.png"))
HEART = pygame.image.load(os.path.join(IMG_DIR, "Other/SmallHeart.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
