
class Job(object):
    def __init__(self, title, salary=1000):
        self.title = title
        self.salary = salary

def show_status(population):
    num_population = len(population)
    print 'Population: %d' % num_population

    if num_population == 0:
        print 'Nobody is left!'
    else:
        print 'Person 0 has $%d' % population[0].money
        print 'Person 0 has %d happiness' % population[0].happiness
