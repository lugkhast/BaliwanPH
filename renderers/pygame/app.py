
import math

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
        self.place_direction = None

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
            self.placing_drag_start = self._px_to_tile_coords(pygame.mouse.get_pos())

    def _mouse_button_released(self, event):
        if event.button is 3:
            self.move_key_active = False
        elif event.button is 1:
            self.is_placing_object = False
            self._clear_overlay()

            self.city.lay_road(self.placing_drag_start, self.placing_last_valid_end)

    def _mark_tiles(self, start_coords, end_coords):
        if start_coords[0] == end_coords[0]:
            # Same X coordinate - vertical road
            x_coord = start_coords[0]
            start_y = start_coords[1]
            end_y = end_coords[1]

            # If we're going up, swap our values for the loop
            if start_y > end_y:
                tmp = start_y
                start_y = end_y
                end_y = tmp

            for i in range(start_y, end_y + 1):
                self.overlay_layer[x_coord][i] = True
        elif start_coords[1] == end_coords[1]:
            y_coord = start_coords[1]
            start_x = start_coords[0]
            end_x = end_coords[0]

            # If we're going left, swap our values for the loop
            if start_x > end_x:
                tmp = start_x
                start_x = end_x
                end_x = tmp

            for i in range(start_x, end_x + 1):
                self.overlay_layer[i][y_coord] = True
        else:
            # Invalid
            print('Invalid start/end coords', start_coords, end_coords)

    def _mouse_moved(self, event):
        if self.move_key_active:
            (cur_x, cur_y) = self.view_offset
            (moved_x, moved_y) = event.rel
            self.view_offset = (cur_x + moved_x, cur_y + moved_y)

        if self.is_placing_object:
            city_size = self.city.dimensions
            mouse_pos = pygame.mouse.get_pos()
            (pos_x, pos_y) = self._px_to_tile_coords(mouse_pos)
            (start_x, start_y) = self.placing_drag_start

            if city_size.x > pos_x >= 0 and city_size.y > pos_y >= 0:
                # The cursor is on a location we can work with
                self._clear_overlay()

                delta_x = math.fabs(start_x - pos_x)
                delta_y = math.fabs(start_y - pos_y)

                if delta_x < delta_y:
                    self.place_direction = 'VERTICAL'
                    road_end_coord = (start_x, pos_y)
                    self._mark_tiles(self.placing_drag_start, road_end_coord)
                else:
                    self.place_direction = 'HORIZONTAL'
                    road_end_coord = (pos_x, start_y)
                    self._mark_tiles(self.placing_drag_start, road_end_coord)

                # Record the adjusted road end coordinate to end up with valid
                # road parameters later
                self.placing_last_valid_end = road_end_coord

    def _key_down(self, event):
        if event.key == K_ESCAPE:
            self.is_placing_object = False
            self._clear_overlay()

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
                elif event.type == KEYDOWN:
                    self._key_down(event)

            if running:
                renderer.get_screen(
                    self.display_surface,
                    self.view_offset,
                    self.overlay_layer,
                    self.place_direction
                )
                pygame.display.update()
                fps_clock.tick(60)
