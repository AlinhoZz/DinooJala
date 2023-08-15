import pygame
import random

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, Y_POS_SMALL_CACTUS, Y_POS_LARGE_CACTUS




class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.random_obs = 0

    def update(self, game):
        if len(self.obstacles) == 0:
            random_obs =  random.randint(0,2)
            self.random_obs = random_obs

            if random_obs == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS, Y_POS_SMALL_CACTUS))

            elif random_obs == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, Y_POS_LARGE_CACTUS))

            elif random_obs == 2:
                self.obstacles.append(Bird(BIRD))   

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)


            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)


    def reset_obstacles(self):
        self.obstacles = []