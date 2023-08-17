from dino_runner.utils.constants import BIRD_Y_POS,BIRD
import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.step_index = 0
        self.adjust_bird_position()

    def adjust_bird_position(self):
        self.bird_type = random.randint(0, 3)
        if self.bird_type == 0:
            self.rect.y = BIRD_Y_POS

        elif self.bird_type == 1:
            self.rect.y = BIRD_Y_POS + 65

        elif self.bird_type == 2:
            self.rect.y = BIRD_Y_POS - 80

        elif self.bird_type == 3:
            self.rect.y = BIRD_Y_POS + 35

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 9:
            self.step_index = 0

