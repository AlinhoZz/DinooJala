import pygame
import os

# Global Constants
TITLE = "Dragon Ball Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 40
BIRD_Y_POS = 260
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets/Other/fundoMusic.mp3")

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
    pygame.image.load(os.path.join(IMG_DIR, "goku/run1blue.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/run2blue.png")),
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
    pygame.image.load(os.path.join(IMG_DIR, "goku/blueaga1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "goku/blueaga2.png")),
]

# Jump
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "goku/pular.png"))
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "goku/pulo1.png")
)
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "goku/bluepulando.png")
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

CN = pygame.image.load(os.path.join(IMG_DIR, "goku/cenario.png"))
CN = pygame.transform.scale(CN, (SCREEN_WIDTH,SCREEN_HEIGHT))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
