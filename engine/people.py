
from random import random

class _PersonConstants(object):
    HAPPINESS_FLOOR = -25
    HAPPINESS_CEILING = 100

    HEALTH_FLOOR = 0
    HEALTH_CEILING = 100

class Person(object):
    _happiness = 50
    _health = _PersonConstants.HEALTH_CEILING

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
    def health(self):
        return self._health
    @health.setter
    def health(self, value):
        minimum = _PersonConstants.HEALTH_FLOOR
        maximum = _PersonConstants.HEALTH_CEILING

        if value < minimum:
            value = minimum
        elif value > maximum:
            value = maximum

        self._health = value
    
    @property
    def happiness(self):
        return self._happiness
    @happiness.setter
    def happiness(self, value):
        if value < _PersonConstants.HAPPINESS_FLOOR:
            value = _PersonConstants.HAPPINESS_FLOOR
        elif value > _PersonConstants.HAPPINESS_CEILING:
            value = _PersonConstants.HAPPINESS_CEILING

        self._happiness = value
    

    def __init__(self, happiness_fuzz=10):
        self.happiness += int(random() * happiness_fuzz) - (happiness_fuzz / 2)
        self.jobs = []
        self.diseases = []
        self._home = None

    def should_be_dead(self):
        return self.health == _PersonConstants.HEALTH_FLOOR
    
    def tick(self):
        for disease in self.diseases:
            disease.apply_effect(self)

        if self.home is None:
            self.happiness -= self.boredom_rate * 5

        for job in self.jobs:
            self.money += job.salary

        if self.should_be_dead():
            self.alive = False
