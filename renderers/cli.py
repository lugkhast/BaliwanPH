
# cli.py
# A command-line renderer for the Baliwan simulator


from StringIO import StringIO


class CLIRenderer(object):

    def __init__(self, city):
        self.city = city

    def get_representation(self, grid_entity):
        if grid_entity == None:
            return '.'

    def get_screen(self):
        grid = self.city.grid
        io = StringIO()

        for row in grid:
            for thing in row:
                symbol = self.get_representation(thing)
                io.write(symbol)
                io.write(' ')
            io.write('\n')

        return io.getvalue()
