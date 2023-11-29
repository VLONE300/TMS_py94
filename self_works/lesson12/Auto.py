import time


class Auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def birthday(self):
        self.age += 1

    def stop(self):
        print('stop')


class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()
        self.load()

    def load(self):
        time.sleep(self.max_load)
        print('load')
        time.sleep(self.max_load)


class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')


truck1 = Truck(brand='Volvo', age=2, color='Red', mark='XC90', weight=5000, max_load='Heavy')
truck2 = Truck(brand='Mercedes', age=3, color='Blue', mark='Sprinter', weight=7000, max_load='Light')

car1 = Car(brand='Toyota', age=1, color='Silver', mark='Camry', weight=3000, max_speed=120)
car2 = Car(brand='Ford', age=5, color='Black', mark='Focus', weight=2500, max_speed=100)
