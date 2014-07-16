#!/usr/bin/env python

# BaliwanPH
# A batshit insane city sim

from random import random

from people import *
from buildings import *
from life import *

population = [Person() for i in range(0, 10)]

for person in population:
    person.jobs.append(Job('Assistant Baliwan Engineer'))

running = True
while running:
    cmd = raw_input('> ')

    for person in population:
        person.tick()

    population = [p for p in population if p.alive]

    print '====='
    show_status(population)

    running = len(population) > 0
