
import pygame
from pygame import Surface
from pygame.locals import *

from engine.city import ZoneType
from .utils.spritesheet import Spritesheet
from .utils.textures import TextureStorage


TOP_OFFSET = 32
DOODAD_OFFSET_Y = -32
TILE_SIZE = 64

class PygameRenderer(object):
    def __init__(self, city):
        self.city = city
        spritesheet = Spritesheet('assets/terrain_0.png')

        self.textures = textures = TextureStorage()
        self._terrain = None

        self.zone_reps = {
            ZoneType.UNZONED: textures.BLANK,
            ZoneType.RESIDENTIAL: textures.ZONE_TILE_RESIDENTIAL,
            ZoneType.COMMERCIAL: textures.ZONE_TILE_COMMERCIAL,
            ZoneType.INDUSTRIAL: textures.ZONE_TILE_INDUSTRIAL
        }

    def _get_tile_px_offset(self, x, y, surface_width):
        # The topmost (top-left) tile is centered by default
        initial_pos_x = surface_width / 2

        # The px calculation is done by first getting the values for the
        # corresponding tile in the first column, then from there we get the
        # offset to the tile we're actually calculating for.

        # Position values for the first column
        base_pos_x = initial_pos_x - (32 * (x + 1))
        base_pos_y = 16 * x

        # Additional offset for the tile we're actually calculating for
        pos_x = base_pos_x + (32 * y)
        pos_y = base_pos_y + (16 * y)

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

    def get_screen(self, surface, offset):
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

        initial_pos_x = width / 2

        surface.fill(pygame.Color(0, 0, 0))

        # Render the landscape layer
        terrain = self.get_terrain()
        # Align the terrain texture with the rest of the world, with offset
        landscape_offset_x = terrain.get_width() / 2 - surface.get_width() / 2
        landscape_offset = (offset[0] - landscape_offset_x, offset[1])
        # Blit with the calculated offset
        surface.blit(terrain, landscape_offset)

        for x in range(0, grid_width):
            pos_x = initial_pos_x - (32 * (x + 1)) + offset[0]
            pos_y = 16 * x + offset[1]
            for y in range(0, grid_height):
                # Render the zone layer
                image = self._get_representation(city.get_tile_at(x, y))
                surface.blit(image, (pos_x, pos_y))

                # Render the doodad layer
                # TODO: Implement actual doodads

                # Increment positions
                pos_x += 32
                pos_y += 16

        return surface
