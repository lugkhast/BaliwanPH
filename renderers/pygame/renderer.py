
import pygame
from pygame import Surface
from pygame.locals import *

from engine.city import ZoneType
from .utils.spritesheet import Spritesheet
from .utils.textures import TextureStorage


TOP_OFFSET = 32
DOODAD_OFFSET_Y = -32
TILE_SIZE = 32

class PygameRenderer(object):
    def __init__(self, city):
        self.city = city

        self.textures = textures = TextureStorage()
        self._terrain = None

        self.zone_reps = {
            ZoneType.UNZONED: textures.BLANK,
            ZoneType.RESIDENTIAL: textures.ZONE_TILE_RESIDENTIAL,
            ZoneType.COMMERCIAL: textures.ZONE_TILE_COMMERCIAL,
            ZoneType.INDUSTRIAL: textures.ZONE_TILE_INDUSTRIAL
        }

    def _get_tile_px_offset(self, x, y, city_surface_width):
        pos_x = x * TILE_SIZE
        pos_y = y * TILE_SIZE

        return (pos_x, pos_y)

    def get_terrain(self):
        if (self._terrain):
            return self._terrain

        # This pixel size calculation assumes a square city area
        # TODO: Handle corner cases needed to support arbitrary city sizes
        size = self.city.dimensions
        surf_width = TILE_SIZE * (size.x + 1)

        # Half of the height of a landscape tile is underground
        # Only the bottom-most landscape tile (the bottom-right corner) has this
        # underground area fully visible.
        surf_height = (surf_width / 2) + (TILE_SIZE / 2)
        surface = Surface((surf_width, surf_height), flags=SRCALPHA)

        for x in range(0, size.x):
            for y in range(0, size.y):
                offset = self._get_tile_px_offset(x, y, surf_width)
                surface.blit(self.textures.LANDSCAPE_PLAINS, offset)

        # surface.fill(pygame.Color(128, 128, 128))
        self._terrain = surface
        return self._terrain

    def _get_representation(self, tile):
        # Use only the RCI bits
        zone_reps = self.zone_reps
        rci_type = tile.zone_type & ZoneType.ALL_TYPES

        if zone_reps.has_key(rci_type):
            return zone_reps[rci_type]
        else:
            print 'Got unknown tile!'
            return self.textures.BLANK

    def get_screen(self, surface, offset, overlay):
        """
        Renders the Baliwan world.

        The rendering system has a concept of layers. All layers of a tile are
        rendered before moving on to the next one. This ensures that z-ordering
        is correct.
        """
        city = self.city
        textures = self.textures
        (width, height) = surface.get_size()
        (grid_width, grid_height) = city.dimensions.as_tuple()

        initial_pos_x = 0

        surface.fill(pygame.Color(0, 0, 0))

        # Render the landscape layer
        terrain = self.get_terrain()
        surface.blit(terrain, offset)

        for x in range(0, grid_width):
            pos_x = (x * 32) + offset[0]
            for y in range(0, grid_height):
                pos_y = (y * 32) + offset[1]
                
                # Render the zone layer
                image = self._get_representation(city.get_tile_at(x, y))
                surface.blit(image, (pos_x, pos_y))

                # Render the overlay
                if overlay[x][y]:
                    surface.blit(self.textures.ROAD_VERTICAL, (pos_x, pos_y))

        return surface
