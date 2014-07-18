#!/usr/bin/env python

# BaliwanPH
# A batshit insane city sim

from random import random

from engine.people import *
from engine.buildings import *
from engine.life import *
from engine.city import City
from renderers.cli import CLIRenderer
from renderers.pygame.app import BaliwanApplication


population = [Person() for i in range(0, 15)]
for person in population:
    person.jobs.append(Job('Assistant Baliwan Engineer'))
    person.diseases.append(Disease('Diabeetus', 10, 5))

size = Dimension(30, 30)
city = City(population, size)
renderer = CLIRenderer(city)
city.zone(0x01, Dimension(0, 0), Dimension(5, 5))
city.zone(0x02, Dimension(6, 6), Dimension(11, 11))

running = True
try:
    # while running:
    #     cmd = raw_input('> ')
    #     city.tick()

    #     print
    #     print '=' * 80
    #     print
    #     print renderer.get_screen()

    #     running = city.get_num_residents() > 0
    baliwan = BaliwanApplication()
    baliwan.start()
except KeyboardInterrupt:
    print
    pass
except EOFError:
    print
    pass
