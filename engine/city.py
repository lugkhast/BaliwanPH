
class ZoneType:
    # The least-significant nibble is used for RCI data
    UNZONED = 0x00

    RESIDENTIAL = 0x01
    COMMERCIAL = 0x02
    INDUSTRIAL = 0x04
    ALL_TYPES = RESIDENTIAL | COMMERCIAL | INDUSTRIAL

    # The second least-significant nibble is used for density
    LOW_DENSITY = 0x10 # Low-density only (b0001)
    MID_DENSITY = 0x30 # Allow both low and medium densities (0011)
    HIGH_DENSITY = 0x70 # Allow low, medium and high densities (0111)


class TerrainTile(object):
    zone_type = None

    def __init__(self, zone_type=ZoneType.UNZONED):
        self.zone_type = zone_type


class City(object):
    def __init__(self, population, dimensions):
        self.population = population or []

        # Generate a size_x by size_y grid of None
        self.grid = [
            [TerrainTile() for x in range(0, dimensions.y)] for x in range(0, dimensions.x)
        ]

        self.dimensions = dimensions

    def zone(self, zone_type, topleft, bottomright):
        grid = self.grid
        x = 0
        y = 0

        x_valid = bottomright.x >= topleft.x
        y_valid = bottomright.y >= topleft.y
        if not (x_valid and y_valid):
            raise ValueError('bottomright coords must be >= topleft coords')

        for row in grid:
            # insert logic here
            if bottomright.y >= y >= topleft.y:
                x = 0
                for tile in row:
                    # insert logic here
                    if bottomright.x >= x >= topleft.x:
                        tile.zone_type = zone_type
                    x += 1
            y += 1

    def tick(self):
        for person in self.population:
            person.tick()

        self.population = [p for p in self.population if p.alive]

    def get_num_residents(self):
        return len(self.population)

    def get_tile_at(self, x, y):
        return self.grid[x][y]

    def print_status(self):
        population = self.population
        num_population = len(population)
        print 'Population: %d' % num_population

        if num_population == 0:
            print 'Nobody is left!'
        else:
            healths = '|'.join([str(p.health) for p in population])
            moneys = '|'.join([str(p.money) for p in population])

            print 'Moneys:  %s' % moneys
            print 'Healths: %s' % healths
