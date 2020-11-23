class Road:
    _length = None
    _width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def mass(self):
        self.weigth = 25
        self.tickness = 0.05
        mass = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'для покрытия всего дорожного полотна нужно {mass} тон')

road_t = Road(20000, 6)
road_t.mass()