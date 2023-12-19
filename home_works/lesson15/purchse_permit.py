from home_works.lesson15.car import Car
from home_works.lesson15.house import House


def house_purchase_permit(person, bank_account, car, house):
    if car:
        if bank_account.amount >= 100:
            bank_account.decrease_money(House.PRICE)
            print("you've successfully purchased a home")
            person.house = house
        else:
            print(f'not enough money to buy a house {bank_account.amount}/100')
    else:
        print('First u need to buy a car')


def car_purchase_permit(person, bank_account, car):
    if bank_account.amount >= 40:
        bank_account.decrease_money(Car.PRICE)
        print("you've successfully purchased a car")
        person.car = car
    else:
        print(f'not enough money to buy a house {bank_account.amount}/40')
