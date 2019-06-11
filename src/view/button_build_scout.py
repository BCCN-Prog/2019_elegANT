import math
import pygame
from .button import Button

from src.settings import all_params


PI = math.pi
STATE_BUTTON = 'add'
STATE_LOADING = 'loading'


class BuildScoutButton(Button):
    def __init__(self, *args, **kwargs):
        super(BuildScoutButton, self).__init__(*args, **kwargs)

        self.state = STATE_BUTTON
        self.counter = 0
        self._loading_angle = 0
        self.color_background = (0, 0, 0)

    def draw(self):
        if self.state == STATE_BUTTON:
            self.draw_add_button()
        elif self.state == STATE_LOADING:
            self.draw_loading()

    def draw_counter(self):
        x = self.x+7
        y = self.y+7
        pygame.draw.circle(self.view.screen, self.color, (x, y), 20)
        # self.view.screen.fill(self.color2, circ)

    def counter_text(self):
        largeText = pygame.font.SysFont('Garamond_Regular.ttf', 30)
        TextSurf = largeText.render(str(self.counter), True, (255,255,255))
        TextRect = TextSurf.get_rect()
        TextRect.center = (self.x + 7, self.y + 7)
        self.view.screen.blit(TextSurf, TextRect)

    def draw_add_button(self):
        rect = [self.x, self.y, self.width, self.height]
        self.view.screen.fill(self.color1, rect, 2)
        image = pygame.transform.scale(pygame.image.load(self.image_path), (self.width, self.height))
        self.view.screen.blit(image, pygame.Rect(self.x, self.y, self.width, self.height))

        # largeText = pygame.font.SysFont('Garamond_Regular.ttf', 120)
        # TextSurf = largeText.render("+", True, (56, 56, 56))
        # TextRect = TextSurf.get_rect()
        # TextRect.center = (self.x + math.floor(self.width / 2), self.y + math.floor(self.height / 2) - 5)
        # self.view.screen.blit(TextSurf, TextRect)

        self.draw_counter()
        self.counter_text()

    def draw_loading(self):
        if self._loading_angle > 360:
            self.state = STATE_BUTTON
            self._loading_angle = 0

        rect = [self.x, self.y, self.width, self.height]
        self.view.screen.fill(self.color1, rect, 2)
        image = pygame.transform.scale(pygame.image.load(self.image_path), (self.width, self.height))
        self.view.screen.blit(image, pygame.Rect(self.x, self.y, self.width, self.height))


        self.draw_counter()

        start = (90 - self._loading_angle) / 180 * PI
        end = PI / 2
        x = self.x-int(self.width/5)
        y = self.y-int(self.height/5)
        rect_load = [x, y, 40, 40]
        self.view.screen.fill(self.color_background, rect_load, 2)
        pygame.draw.arc(self.view.screen, self.color2, rect_load, start, end, 19)
        denominator_angle = all_params.controller_params.framerate * all_params.controller_params.create_ant_time
        self._loading_angle += 360 / denominator_angle

        self.counter_text()

