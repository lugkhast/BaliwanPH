
import pygame
from pygame.locals import *

class BaliwanApplication(object):
    def __init__(self):
        pygame.init()

    def start(self):
        self.display_surface = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('BaliwanPH')

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    running = False

            if running:
                pygame.display.update()
