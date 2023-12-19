from home_works.lesson15.car import Car
from home_works.lesson15.house import House
from home_works.lesson15.human import Human


def app():
    bob = Human('Bob', '0987654321')
    house = House('Beverly Hills 9')
    car = Car('BMW', 'i8')
    for i in range(25):
        bob.work()
    bob.buy(car)
    print(bob.car)
    bob.buy(house)
    print(bob.house)
    bob.sell(car)
    bob.sell(house)

app()
