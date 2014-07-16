
from random import random

class Person(object):
    happiness = 50
    intellect = 0
    money = 0

    boredom_rate = 1

    def __init__(self, happiness_fuzz=10):
        self.happiness += int(random() * happiness_fuzz) - (happiness_fuzz / 2)
        self.jobs = []

    def tick(self):
        self.happiness -= self.boredom_rate

        for job in self.jobs:
            self.money += job.salary

