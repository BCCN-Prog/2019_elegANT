import pygame
from ui_element import UIElement

class InputBox(UIElement):

    def __init__(self, view, identifier, x, y, width, height, color1, color2, text=''):
        super(InputBox, self).__init__(view, identifier, x, y, width, height)
        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        self.text = text
        self.txt_surface = self.view.FONT.render(text, True, self.color)
        self.active = False
        self.on("mouseclick", self.mouse_click, self.color2)
        self.on("keyret", self.keyret, self.text)
        self.on("keyback", self.keyback, self.text)

    def mouse_click(self, newcolor):
        self.active = not self.active
        self.color = newcolor

    def keyret(self, text):
        print(text)
        self.text = ''

    def keyback(self, text):
        self.text = text[:-1]

    def event_handler(self, event):
        pygame.init()
        pos = self.view.mouse_pos
        # m_down = self.view.mouse_down
        # m_event = self.view.mouse_event
        # k_return = self.view.key_return
        # k_down = self.view.key_keydown
        # k_backspace = self.view.key_back

        # for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pos):
                if "mouseclick" in self.events:
                    for fnct, args in self.events["mouseclick"]:
                        fnct(args)
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    print('back loop')
                    # if "keyret" in self.events:
                    #     for fnct, args in self.events["keyret"]:
                    #         fnct(args)
                if event.key == pygame.K_RETURN:
                    print('ret loop')
                    # if "keyback" in self.events:
                    #     for fnct, args in self.events["keyback"]:
                    #         fnct(args)
                else:
                    # print('Print text')
                    self.text += event.unicode
                self.txt_surface = self.view.FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self):
        self.view.screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(self.view.screen, self.color, self.rect, 2)