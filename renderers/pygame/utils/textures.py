
from pygame import Surface

from .spritesheet import SizedSpritesheet

class TextureStorage(object):
    def create_easy_texture(self, color):
        surface = Surface((32, 32))
        surface.fill(color)

    def __init__(self):
        spritesheet = SizedSpritesheet('assets/flatass.png', (32, 32))

        self.BLANK = spritesheet.image_at(0, 1)
        self.LANDSCAPE_PLAINS = spritesheet.image_at(2, 0)
        
        self.DOODAD_GRASS_THICK = spritesheet.image_at(4, 11)
        self.DOODAD_BUSH_SMALL = spritesheet.image_at(6, 12)
        self.DOODAD_BUSH_LARGE = spritesheet.image_at(7, 12)

        self.ZONE_TILE_RESIDENTIAL = spritesheet.image_at(5, 1)
        self.ZONE_TILE_COMMERCIAL = spritesheet.image_at(6, 1)
        self.ZONE_TILE_INDUSTRIAL = spritesheet.image_at(7, 1)

        self.ROAD_SINGLE = spritesheet.image_at(7, 2)
        self.ROAD_VERTICAL = spritesheet.image_at(1, 2)
        self.ROAD_HORIZONTAL_END_RIGHT = spritesheet.image_at(4, 3)
        self.ROAD_HORIZONTAL_END_LEFT = spritesheet.image_at(6, 3)
        self.ROAD_VERTICAL_END_TOP = spritesheet.image_at(7, 3)
        self.ROAD_VERTICAL_END_BOTTOM = spritesheet.image_at(5, 3)

        self.ROAD_INTERSECTION = spritesheet.image_at(2, 2)
        self.ROAD_T_SOUTH = spritesheet.image_at(3, 2)
        self.ROAD_T_WEST = spritesheet.image_at(4, 2)
        self.ROAD_T_NORTH = spritesheet.image_at(5, 2)
        self.ROAD_T_EAST = spritesheet.image_at(6, 2)

        self.ROAD_L_SOUTH_WEST = spritesheet.image_at(0, 3)
        self.ROAD_L_NORTH_WEST = spritesheet.image_at(1, 3)
        self.ROAD_L_NORTH_EAST = spritesheet.image_at(2, 3)
        self.ROAD_L_SOUTH_EAST = spritesheet.image_at(3, 3)

        self.ROAD_HORIZONTAL = spritesheet.image_at(0, 2)

        self.FLAT_GRASS = spritesheet.image_at(1, 0)

