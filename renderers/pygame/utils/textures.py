
from renderers.pygame.utils.spritesheet import SizedSpritesheet

class TextureStorage(object):
    def __init__(self):
        spritesheet = SizedSpritesheet('assets/terrain_0.png', (64, 64))

        self.BLANK = spritesheet.image_at(0, 0)
        self.LANDSCAPE_PLAINS = spritesheet.image_at(1, 0)
        
        self.DOODAD_GRASS_THICK = spritesheet.image_at(4, 11)
        self.DOODAD_BUSH_SMALL = spritesheet.image_at(6, 12)
        self.DOODAD_BUSH_LARGE = spritesheet.image_at(7, 12)
