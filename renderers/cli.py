
# cli.py
# A command-line renderer for the Baliwan simulator


from StringIO import StringIO

from engine.city import ZoneType


class CLIRenderer(object):

    _zone_representations = {
        ZoneType.UNZONED: '.',
        ZoneType.ALL_TYPES: 'a',
        ZoneType.RESIDENTIAL: 'r',
        ZoneType.COMMERCIAL: 'c',
        ZoneType.INDUSTRIAL: 'i'
    }

    def __init__(self, city):
        self.city = city

    def _get_representation(self, tile):
        zone_reps = self._zone_representations

        # Use only the RCI bits
        rci_type = tile.zone_type & ZoneType.ALL_TYPES

        if zone_reps.has_key(rci_type):
            return zone_reps[rci_type]
        else:
            return '?'

    def get_screen(self):
        grid = self.city.grid
        io = StringIO()

        for row in grid:
            for thing in row:
                symbol = self._get_representation(thing)
                io.write(symbol)
                io.write(' ')
            io.write('\n')

        return io.getvalue()
