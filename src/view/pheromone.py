import pygame
from .view_element import ViewElement


class Pheromone(ViewElement):
    def __init__(self, view, identifier, x, y, strength, color):
        super().__init__(view, identifier, x, y, width=4, height=4)
        self.z_index = 4
        self.strength = strength
        self.color = (0, 0, 0)

    def draw(self):
        pygame.draw.rect(self.view.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        