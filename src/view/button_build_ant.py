import math
import pygame
from .button import Button

from src.settings import all_params


PI = math.pi
STATE_BUTTON = 'add'
STATE_LOADING = 'loading'


class BuildAntButton(Button):
    def __init__(self, ant_type, *args, **kwargs):
        super(BuildAntButton, self).__init__(*args, **kwargs)

        self.ant_type = ant_type
        self.state = STATE_BUTTON
        self.counter = 0
        self._loading_angle = 0
        self.color_background = (0, 0, 0)
        self.color = (219, 87, 178)
        name = "_".join((str(c) for c in self.color))
        self.image = pygame.image.load(f"src/view/images/{name}_buildscout.png")

    def draw(self):
        if self.state == STATE_BUTTON:
            self.draw_add_button()
        elif self.state == STATE_LOADING:
            self.draw_loading()

    def draw_add_button(self):
        super(BuildAntButton, self).draw()
        loc = self.image.get_rect().center
        loc = (self.x - 10, self.y - 10)
        self.view.screen.blit(self.image, loc)

        self.draw_counter()
        self.counter_text()

    def draw_loading(self):
        super(BuildAntButton, self).draw()
        if self._loading_angle > 360:
            self.state = STATE_BUTTON
            self._loading_angle = 0

        loc = self.image.get_rect().center
        loc = (self.x - 10, self.y - 10)
        self.view.screen.blit(self.image, loc)

        self.draw_counter()

        start = (90 - self._loading_angle) / 180 * PI
        end = PI / 2
# <<<<<<< HEAD:src/view/button_build_scout.py
        x = self.x - int(self.width / 5)
        y = self.y - int(self.height / 5)
        rect_load = [x, y, 40, 40]
        self.view.screen.fill(self.color_background, rect_load, 2)
        pygame.draw.arc(self.view.screen, self.color2, rect_load, start, end, 19)
# =======
#         rect = [self.x, self.y, self.width, self.height]
#         self.view.screen.fill(self.color1, rect, 2)
#
#         arc_width = int(min(self.width, self.height) / 2)
#
#         pygame.draw.arc(self.view.screen, self.color2, rect, start, end, arc_width)
# >>>>>>> master:src/view/button_build_ant.py
        denominator_angle = all_params.controller_params.framerate * all_params.controller_params.create_ant_time
        self._loading_angle += 360 / denominator_angle

        self.counter_text()

    def draw_counter(self):
        x = self.x + 5
        y = self.y + 5
        pygame.draw.circle(self.view.screen, self.color, (x, y), 20)

    def counter_text(self):
        largeText = pygame.font.SysFont('Garamond_Regular.ttf', 30)
        TextSurf = largeText.render(str(self.counter), True, (255, 255, 255))
        TextRect = TextSurf.get_rect()
        TextRect.center = (self.x + 7, self.y + 7)
        self.view.screen.blit(TextSurf, TextRect)





