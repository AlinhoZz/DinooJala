import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD_Y_POS, BIRD

class Bird(Obstacle):
    def __init__(self, images):
        super().__init__(images, 0)
        self.step_index = 0
        self.bird_type = random.randint(0,3)
        if self.bird_type == 0:
            self.rect.y = BIRD_Y_POS

        elif self.bird_type == 1:
            self.rect.y = BIRD_Y_POS + 50

        elif self.bird_type == 2:
            self.rect.y = BIRD_Y_POS - 80

        elif self.bird_type == 3:
            self.rect.y = BIRD_Y_POS + 35    

   
    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]

        self.bird_rect = self.image.get_rect()
        self.step_index += 1

        if self.step_index >=10:
            self.step_index = 0

    def update(self, game_speed, obstacles):
        self.fly()
        super().update(game_speed, obstacles)