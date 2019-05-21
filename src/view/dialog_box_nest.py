from dialog_box import DialogBox
from slider import Slider
import pygame


class DialogBoxNest(DialogBox):
    def __init__(self, view, identifier, properties, active="False"):
        super(DialogBoxNest, self).__init__(view, identifier, x=view.size[0] * 0.75, y=0,
                                            width=view.size[0]*0.25, height=view.size[1])
        self.properties = properties
        self.active = active
        self.identifier = identifier
        self.sliders = []
        self.set_sliders()
        self.on('click', self.click)

    def click(self):
        self.active = True

    def set_sliders(self):
        for i, (key, value) in enumerate(self.properties.items()):
            self.sliders.append(Slider(self.view, f"slider_{key}", value, self.x + 5, self.y + 50 + 100*i,
                                       self.width * 0.80, 20, name=key))

    def draw(self):
        if self.active:
            pygame.draw.rect(self.view.screen, pygame.Color("black"), self.rect, 2)
            for slider in self.sliders:
                self.view.add_element(slider)
        else:
            for slider in self.sliders:
                self.view.remove_element(slider.identifier)
            self.view.remove_element(self.identifier)