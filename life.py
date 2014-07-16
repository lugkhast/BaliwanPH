
from random import random

class Job(object):
    def __init__(self, title, salary=1000):
        self.title = title
        self.salary = salary


class Disease(object):
    """
    A Disease causes damage on a Person, as determined by the base damage and
    fuzz parameters. "fuzz" is the size of the interval centered at damage in
    which the final calculated damage will be randomly determined.

    Quirk: Given a small enough base damage/large enough fuzz, a disease can
    randomly cause an increase in health. This is intentional.
    """
    def __init__(self, name, base_damage, fuzz=0):
        self.name = name
        self.base_damage = base_damage
        self.fuzz = fuzz

    def apply_effect(self, person):
        fuzz = self.fuzz
        
        final_fuzz = (random() * fuzz) - (fuzz / 2)
        final_damage = self.base_damage + (random() * fuzz) - (fuzz / 2)

        person.health -= int(final_damage)
