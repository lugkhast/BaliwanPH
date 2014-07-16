#!/usr/bin/env python

# BaliwanPH
# A batshit insane city sim

from random import random

from people import *
from buildings import *
from life import *
from city import City


population = [Person() for i in range(0, 15)]
for person in population:
    person.jobs.append(Job('Assistant Baliwan Engineer'))
    person.diseases.append(Disease('Diabeetus', 10, 5))

city = City(population=population)

running = True
while running:
    cmd = raw_input('> ')
    city.tick()

    print '====='
    city.print_status()

    running = city.get_num_residents() > 0
