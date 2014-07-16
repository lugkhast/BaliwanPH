#!/usr/bin/env python

# BaliwanPH
# A batshit insane city sim

from random import random

from people import *

class Dimension(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class BuildingClass(object):
    RESIDENTIAL             = 'residential'
    COMMERCIAL_SERVICE      = 'commercial-service'
    COMMERCIAL_OFFICE       = 'commercial-office'


class Building(object):
    capacity = 1
    
    def __init__(self, bldg_class, capacity):
        self.size = Dimension(10, 10)
        self.capacity = capacity
        self._occupants = []

    def is_full(self):
        return len(self._occupants) >= self.capacity


class Job(object):
    def __init__(self, title, salary=1000):
        self.title = title
        self.salary = salary


population = [Person() for i in range(0, 10)]

for person in population:
    person.jobs.append(Job('Assistant Baliwan Engineer'))


def show_status():
    print 'Population: %d' % len(population)
    print 'Person 0 has $%d' % population[0].money


running = True

while running:
    cmd = raw_input('> ')

    for person in population:
        person.tick()

    print '====='
    show_status()
