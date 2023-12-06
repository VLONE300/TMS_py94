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
