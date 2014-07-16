#!/usr/bin/env python

# BaliwanPH
# A batshit insane city sim

from random import random

from engine.people import *
from engine.buildings import *
from engine.life import *
from engine.city import City
from renderers.cli import CLIRenderer


population = [Person() for i in range(0, 15)]
for person in population:
    person.jobs.append(Job('Assistant Baliwan Engineer'))
    person.diseases.append(Disease('Diabeetus', 10, 5))

size = Dimension(30, 30)
city = City(population, size)

running = True
while running:
    cmd = raw_input('> ')
    city.tick()

    print
    print '=' * 80
    print
    renderer = CLIRenderer(city)
    print renderer.get_screen()

    running = city.get_num_residents() > 0
