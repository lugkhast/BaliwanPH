
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
    road_size = 0

    def __init__(self, zone_type=ZoneType.UNZONED):
        self.zone_type = zone_type

    def place_road(self, is_big=False):
        self.zone_type = ZoneType.UNZONED

        if is_big:
            self.road_size = 2
        else:
            self.road_size = 1

    def has_road(self):
        return self.road_size > 0


class City(object):
    def __init__(self, population, dimensions):
        self.population = population or []

        # Generate a size_x by size_y grid of None
        # This is NOT in row major order, so access it with grid[X][Y]
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

    def lay_road(self, start, end, is_big=False):
        (start_x, start_y) = start
        (end_x, end_y) = end

        print('Laying road from', start, 'to', end)

        if start_x == end_x:
            # Vertical!
            if start_y > end_y:
                (start_y, end_y) = (end_y, start_y)

            for i in range(start_y, end_y + 1):
                self.grid[start_x][i].place_road(is_big=is_big)
        elif start_y == end_y:
            # Horizontal!
            if start_x > end_x:
                (start_x, end_x) = (end_x, start_x)

            for i in range(start_x, end_x + 1):
                self.grid[i][start_y].place_road(is_big=is_big)
        else:
            print 'Received invalid road parameters!'

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
