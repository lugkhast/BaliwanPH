
class City(object):
    def __init__(self, population=None, size_x=100, size_y=100):
        self.population = population or []

        # Generate a size_x by size_y grid of None
        self.grid = [
            [None for x in range(0, size_y)] for x in range(0, size_x)
        ]

    def tick(self):
        for person in self.population:
            person.tick()

        self.population = [p for p in self.population if p.alive]

    def get_num_residents(self):
        return len(self.population)

    def print_status(self):
        population = self.population
        num_population = len(population)
        print 'Population: %d' % num_population

        if num_population == 0:
            print 'Nobody is left!'
        else:
            print 'Person 0 has $%d' % population[0].money
            print 'Person 0 has %d health' % population[0].health
