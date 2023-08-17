import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_types = [
            Cactus,
            Bird,
        ]
        if len(self.obstacles) == 0:
            obstacle_class = random.choice(obstacle_types)
            self.obstacles.append(obstacle_class())

        obstacles_to_remove = []

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.type == SHIELD_TYPE and isinstance(obstacle, Cactus):
                    obstacles_to_remove.append(obstacle)
                elif game.player.type == HAMMER_TYPE and isinstance(obstacle, Bird):
                    obstacles_to_remove.append(obstacle)
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break

        for obstacle in obstacles_to_remove:
            self.obstacles.remove(obstacle)
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []