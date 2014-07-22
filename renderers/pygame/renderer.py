
import pygame
from pygame.locals import *

from engine.city import ZoneType
from renderers.pygame.utils.spritesheet import Spritesheet
from renderers.pygame.utils.textures import TextureStorage


TOP_OFFSET = 32
DOODAD_OFFSET_Y = -32

class PygameRenderer(object):
    def __init__(self, city):
        self.city = city
        spritesheet = Spritesheet('assets/terrain_0.png')

        self.textures = textures = TextureStorage()

        self.zone_reps = {
            ZoneType.UNZONED: textures.BLANK,
            ZoneType.RESIDENTIAL: textures.ZONE_TILE_RESIDENTIAL,
            ZoneType.COMMERCIAL: textures.ZONE_TILE_COMMERCIAL,
            ZoneType.INDUSTRIAL: textures.ZONE_TILE_INDUSTRIAL
        }

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
        for x in range(0, grid_width):
            pos_x = initial_pos_x - (32 * x) + offset[0]
            pos_y = 16 * x + offset[1]
            for y in range(0, grid_height):
                # Render the landscape layer
                surface.blit(textures.LANDSCAPE_PLAINS, (pos_x, pos_y))

                # Render the zone layer
                image = self._get_representation(city.get_tile_at(x, y))
                surface.blit(image, (pos_x, pos_y))

                # Render the doodad layer
                # TODO: Implement actual doodads

                # Increment positions
                pos_x += 32
                pos_y += 16

        return surface
