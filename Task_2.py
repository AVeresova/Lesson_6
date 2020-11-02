class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def weight_asphalt(self):
        weight_asphalt = self._length * self._width * self.weight * self.height / 1000
        print(f'Расчет массы асфальта для покрытия всего дорожного полотна: {weight_asphalt} тонн')


r = Road(20, 5000)
r.weight_asphalt()