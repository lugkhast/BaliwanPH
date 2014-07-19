
import pygame
from pygame.locals import *

from renderers.pygame.renderer import PygameRenderer

class BaliwanApplication(object):
    def __init__(self, city):
        pygame.init()
        self.city = city

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

            if running:
                renderer.get_screen(self.display_surface)
                pygame.display.update()
                fps_clock.tick(30)