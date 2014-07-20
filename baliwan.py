#!/usr/bin/env python

# BaliwanPH
# A batshit insane city sim

from random import random

from engine.people import *
from engine.buildings import *
from engine.life import *
from engine.city import City, ZoneType
from renderers.cli import CLIRenderer
from renderers.pygame.app import BaliwanApplication


population = [Person() for i in range(0, 15)]
for person in population:
    person.jobs.append(Job('Assistant Baliwan Engineer'))
    person.diseases.append(Disease('Diabeetus', 10, 5))

size = Dimension(30, 30)
city = City(population, size)
renderer = CLIRenderer(city)
city.zone(ZoneType.RESIDENTIAL, Dimension(0, 0), Dimension(5, 5))
city.zone(ZoneType.COMMERCIAL, Dimension(6, 6), Dimension(11, 11))
city.zone(ZoneType.INDUSTRIAL, Dimension(6, 0), Dimension(11, 5))

running = True
try:
    baliwan = BaliwanApplication(city)
    baliwan.start()
except KeyboardInterrupt:
    print
    pass
except EOFError:
    print
    pass
