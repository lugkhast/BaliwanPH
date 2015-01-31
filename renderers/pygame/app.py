
import pygame
from pygame.locals import *

from renderers.pygame import renderer
from renderers.pygame.renderer import PygameRenderer

class BaliwanApplication(object):
    def __init__(self, city):
        pygame.init()
        self.city = city

        self.move_key_active = False
        self.is_placing_object = False
        self.placing_drag_start = None

        self.view_offset = (0, 0)

        city_size = city.dimensions
        self.overlay_layer = [
            [None for x in range(0, city_size.y)] for x in range(0, city_size.x)
        ]

    def _clear_overlay(self):
        city_size = self.city.dimensions
        for i in range(0, city_size.x):
            for j in range(0, city_size.y):
                self.overlay_layer[i][j] = None

    def _px_to_tile_coords(self, px_tuple):
        (xpix, ypix) = px_tuple
        view_offset = self.view_offset

        (offsetted_x, offseted_y) = (xpix - view_offset[0], ypix - view_offset[1])

        tile_size = renderer.TILE_SIZE
        return (offsetted_x / tile_size, offseted_y / tile_size)

    def _mouse_button_pressed(self, event):
        if event.button is 3:
            self.move_key_active = True
        elif event.button is 1:
            self.is_placing_object = True

    def _mouse_button_released(self, event):
        if event.button is 3:
            self.move_key_active = False
        elif event.button is 1:
            self.is_placing_object = False
            self._clear_overlay()

    def _mouse_moved(self, event):
        if self.move_key_active:
            (cur_x, cur_y) = self.view_offset
            (moved_x, moved_y) = event.rel
            self.view_offset = (cur_x + moved_x, cur_y + moved_y)

        if self.is_placing_object:
            city_size = self.city.dimensions
            mouse_pos = pygame.mouse.get_pos()
            (pos_x, pos_y) = self._px_to_tile_coords(mouse_pos)

            if city_size.x > pos_x > 0 and city_size.y > pos_y > 0:
                self.overlay_layer[pos_x][pos_y] = True

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
                renderer.get_screen(
                    self.display_surface,
                    self.view_offset,
                    self.overlay_layer
                )
                pygame.display.update()
                fps_clock.tick(60)
