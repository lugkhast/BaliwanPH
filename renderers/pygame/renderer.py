
import pygame
from pygame.locals import *

from engine.city import ZoneType
from renderers.pygame.utils.spritesheet import Spritesheet


TOP_OFFSET = 32

class PygameRenderer(object):
    def __init__(self, city):
        self.city = city
        spritesheet = Spritesheet('assets/terrain_0.png')

        self.plains = plains = spritesheet.image_at((64 * 2, 0, 64, 64))
        self.rocks = rocks = spritesheet.image_at((64 * 0, 64 * 5, 64, 64))
        self.grass = grass = spritesheet.image_at((64 * 4, 64 * 11, 64, 64))

        self.textures = {
            ZoneType.UNZONED: plains,
            ZoneType.RESIDENTIAL: grass,
            ZoneType.COMMERCIAL: rocks
        }

    def _get_representation(self, tile):
        # Use only the RCI bits
        zone_reps = self.textures
        rci_type = tile.zone_type & ZoneType.ALL_TYPES

        if zone_reps.has_key(rci_type):
            return zone_reps[rci_type]
        else:
            return plains

    def get_screen(self, surface):
        city = self.city
        (width, height) = surface.get_size()
        (grid_width, grid_height) = city.dimensions.as_tuple()

        initial_pos_x = width / 2

        for x in range(0, grid_width):
            pos_x = initial_pos_x - (32 * x)
            pos_y = 16 * x + TOP_OFFSET
            for y in range(0, grid_height):
                image = self._get_representation(city.get_tile_at(x, y))

                surface.blit(image, (pos_x, pos_y))
                pos_x += 32
                pos_y += 16

        return surface
