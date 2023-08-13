import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD_Y_POS, BIRD

class Bird(Obstacle):
    def __init__(self, images):
        super().__init__(images, 0)
        self.step_index = 0
        self.bird_type = random.randint(0,1)
        if type == 0:
            self.rect.y = BIRD_Y_POS
        else:
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