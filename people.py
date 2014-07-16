
from random import random

class Person(object):
    HAPPINESS_FLOOR = -25
    HAPPINESS_CEILING = 100

    _happiness = 50

    intellect = 0
    money = 0
    alive = True

    boredom_rate = 1

    @property
    def home(self):
        return self._home

    @home.setter
    def home(self, value):
        self._home = value

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if value < self.HAPPINESS_FLOOR:
            value = self.HAPPINESS_FLOOR
        elif value > self.HAPPINESS_CEILING:
            value = self.HAPPINESS_CEILING

        self._happiness = value
    

    def __init__(self, happiness_fuzz=10):
        self.happiness += int(random() * happiness_fuzz) - (happiness_fuzz / 2)
        self.jobs = []
        self.home = None

    def should_be_dead(self):
        return self.happiness == self.HAPPINESS_FLOOR
    
    def tick(self):
        self.happiness -= self.boredom_rate

        if self.home is None:
            self.happiness -= self.boredom_rate * 5

        for job in self.jobs:
            self.money += job.salary

        if self.should_be_dead():
            self.alive = False
