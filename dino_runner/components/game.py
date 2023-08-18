import pygame

from pygame import mixer

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, CN, MUSIC_DIR
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.text_utils import draw_message_component

FONT_STYLE = "freesansbold.ttf"
TEXT_COLOR_ORANGE =  (255, 140, 0) 

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.x_pos_fundopy = 0
        self.y_pos_fundopy = 0
        self.game_speed = 20
        self.score = 0
        self.color_counter = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()


    def reset_game(self):
        self.player = Dinosaur()
        mixer.music.stop()
        mixer.music.play(-1)
        self.obstacle_manager.reset_obstacles()
        self.game_speed = 20
        self.score = 0 
        self.color_counter = 0

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def fase(self):
        if self.score < 200 * (self.color_counter + 1):
            if self.color_counter % 2 == 0:
                self.screen.fill((135, 206, 235))
            else:
                self.screen.fill((0, 0, 128))
        else:
            self.color_counter += 1
        

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 1

    def draw(self):
        self.clock.tick(FPS)
        self.draw_fundopy()
        self.fase()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()


    def draw_fundopy(self):
        image_width = CN.get_width()
        self.screen.blit(CN, (self.x_pos_fundopy, self.y_pos_fundopy))
        self.screen.blit(CN, (image_width + self.x_pos_fundopy, self.y_pos_fundopy))
        if self.x_pos_fundopy <= -image_width:
            self.screen.blit(CN, (image_width + self.x_pos_fundopy, self.y_pos_fundopy))
            self.x_pos_fundopy = 0
        x = 0.1
        self.x_pos_fundopy -= (2 - x)


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg == self.game_speed


    def draw_score(self):
        draw_message_component(
            f"Score: {self.score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=50,
            font_color= (255, 165, 0),
        )

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 1)
            if time_to_show >= 0:
                draw_message_component(
                    f" Tempo de PowerUp restante: {time_to_show} segundos",
                    self.screen,
                    font_size=18,
                    font_color = TEXT_COLOR_ORANGE,
                    pos_x_center=550,
                    pos_y_center=40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def pos_menu(self, text, Y , font_size, color):
        half_screen_width = SCREEN_WIDTH //2
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, Y)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        pygame.mixer.music.load(MUSIC_DIR)
        novo_volume = 0.02
        mixer.music.set_volume(novo_volume)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count > 0:
            self.pos_menu(f"Partidas jogadas:  {self.death_count}", half_screen_height + 55, 18,(TEXT_COLOR_ORANGE))
            self.pos_menu(f"Sua Pontuação:  {self.score}", half_screen_height + 80, 18,(TEXT_COLOR_ORANGE))

        if self.death_count == 0:  # Tela de inicio
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Aperte Qualquer Tecla para Iniciar.  (Semente verde desvia de tudo, menos do Majin Boo!)", True, TEXT_COLOR_ORANGE)
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        else:  # Tela de restart
            self.screen.blit(ICON, (half_screen_width - 140, half_screen_height - 140))
        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
