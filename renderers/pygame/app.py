
import pygame
from pygame.locals import *

from renderers.pygame.renderer import PygameRenderer

class BaliwanApplication(object):
    def __init__(self, city):
        pygame.init()
        self.city = city
        self.move_key_active = False
        self.view_offset = (0, 0)

    def _mouse_button_pressed(self, event):
        if event.button is 3:
            self.move_key_active = True

    def _mouse_button_released(self, event):
        if event.button is 3:
            self.move_key_active = False

    def _mouse_moved(self, event):
        if self.move_key_active:
            (cur_x, cur_y) = self.view_offset
            (moved_x, moved_y) = event.rel
            self.view_offset = (cur_x + moved_x, cur_y + moved_y)

    def start(self):
        self.display_surface = pygame.display.set_mode((1024, 600))
        pygame.display.set_caption('BaliwanPH')
        renderer = PygameRenderer(self.city)

        fps_clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    self._mouse_button_pressed(event)
                elif event.type == MOUSEBUTTONUP:
                    self._mouse_button_released(event)
                elif event.type == MOUSEMOTION:
                    self._mouse_moved(event)

            if running:
                renderer.get_screen(self.display_surface, self.view_offset)
                pygame.display.update()
                fps_clock.tick(60)
