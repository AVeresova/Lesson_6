class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} начал движение'

    def stop(self):
        return f'\n Автомобиль {self.name} остановился'

    def turn(self, direction):
        return f'\n Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nСкорость автомобиля {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n Скорость превышена! Более 60 км/ч'
        else:
            return f'\т Скорость в пределах нормы'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Скорость превышена! Более 40 км/ч'


class PoliceCar(Car):
    pass


town = TownCar('Ford', 70, 'черный', False)
print('\n' + town.show_speed())

sport = SportCar('Subaru', 100, 'желтый', False)
print('\n' + sport.show_speed())

work = WorkCar('Фургон', 30, 'белый', False)
print('\n' + work.show_speed())

police = PoliceCar('Ford', 100, 'белый', True)
print('\n' + police.show_speed())
