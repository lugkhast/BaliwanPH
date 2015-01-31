
from pygame import Surface

from .spritesheet import SizedSpritesheet

class TextureStorage(object):
    def create_easy_texture(self, color):
        surface = Surface((32, 32))
        surface.fill(color)

    def __init__(self):
        spritesheet = SizedSpritesheet('assets/flatass.png', (32, 32))

        self.BLANK = spritesheet.image_at(2, 0)
        self.LANDSCAPE_PLAINS = spritesheet.image_at(2, 0)
        
        self.DOODAD_GRASS_THICK = spritesheet.image_at(4, 11)
        self.DOODAD_BUSH_SMALL = spritesheet.image_at(6, 12)
        self.DOODAD_BUSH_LARGE = spritesheet.image_at(7, 12)

        self.ZONE_TILE_RESIDENTIAL = spritesheet.image_at(5, 1)
        self.ZONE_TILE_COMMERCIAL = spritesheet.image_at(6, 1)
        self.ZONE_TILE_INDUSTRIAL = spritesheet.image_at(7, 1)

        self.FLAT_GRASS = spritesheet.image_at(1, 0)

