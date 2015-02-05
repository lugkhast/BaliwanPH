
from __future__ import print_function


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
    
    # Road-related data
    road_size = 0
    road_north = False
    road_south = False
    road_east = False
    road_west = False

    def __init__(self, zone_type=ZoneType.UNZONED):
        self.reset()
        self.zone_type = zone_type

    def reset(self):
        """
        Puts a TerrainTile into its default state
        """
        self.zone_type = None
        self.road_size = 0
        self.road_north = False
        self.road_south = False
        self.road_east = False
        self.road_west = False

    def place_road(self, is_big=False):
        self.zone_type = ZoneType.UNZONED

        if is_big:
            self.road_size = 2
        else:
            self.road_size = 1

    def has_road(self):
        return self.road_size > 0

    def update_road_adjacency(self, grid, coord):
        grid_width = len(grid)
        grid_height = len(grid[0])
        (x, y) = coord
        center_tile = grid[x][y]

        if x > 0:
            other_tile = grid[x - 1][y]
            if other_tile.has_road(): 
                other_tile.road_east = True
                center_tile.road_west = True

        if x < grid_width - 1:
            other_tile = grid[x + 1][y]
            if other_tile.has_road():
                other_tile.road_west = True
                center_tile.road_east = True

        if y > 0:
            other_tile = grid[x][y - 1]
            if other_tile.has_road():
                other_tile.road_south = True
                center_tile.road_north = True

        if y < grid_height - 1:
            other_tile = grid[x][y + 1]
            if other_tile.has_road():
                other_tile.road_north = True
                center_tile.road_south = True


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

    def update_road_adjacency(self, coord):
        (x, y) = coord
        center_tile = self.grid[x][y]
        center_tile.update_road_adjacency(self.grid, coord)

    def lay_road(self, start, end, is_big=False):
        (start_x, start_y) = start
        (end_x, end_y) = end

        print('Laying road from', start, 'to', end)

        if start_x == end_x:
            # Vertical!
            if start_y > end_y:
                (start_y, end_y) = (end_y, start_y)

            for i in range(start_y, end_y + 1):
                tile = self.grid[start_x][i]
                tile.place_road(is_big=is_big)
                self.update_road_adjacency((start_x, i))
        elif start_y == end_y:
            # Horizontal!
            if start_x > end_x:
                (start_x, end_x) = (end_x, start_x)

            for i in range(start_x, end_x + 1):
                tile = self.grid[i][start_y]
                tile.place_road(is_big=is_big)
                self.update_road_adjacency((i, start_y))
        else:
            print('Received invalid road parameters!')

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
        print('Population: %d' % num_population)

        if num_population == 0:
            print('Nobody is left!')
        else:
            healths = '|'.join([str(p.health) for p in population])
            moneys = '|'.join([str(p.money) for p in population])

            print('Moneys:  %s' % moneys)
            print('Healths: %s' % healths)
