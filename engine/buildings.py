
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
