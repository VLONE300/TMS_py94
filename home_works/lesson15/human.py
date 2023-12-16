from random import randint

from home_works.lesson15.bank_account import BankAccount
from home_works.lesson15.house import House
from home_works.lesson15.car import Car
from home_works.lesson15.purchse_permit import house_purchase_permit, car_purchase_permit


class Human:
    created_passport_nums = set()

    def __init__(self, name, passport_id):
        if passport_id in self.created_passport_nums:
            raise ValueError('...')

        self.name = name
        self.passport_id = passport_id
        self.__bank_account = BankAccount(self.passport_id)
        self.house = None
        self.car = None

    def __repr__(self):
        return f'{self.name, self.passport_id}'

    def work(self):
        salary = randint(5, 11)
        self.__bank_account.increase_money(salary)

    def buy(self, choice):
        if isinstance(choice, House):
            return house_purchase_permit(self, self.__bank_account, self.car, choice)
        elif isinstance(choice, Car):
            return car_purchase_permit(self, self.__bank_account, choice)
        else:
            print('You cant buy this')

    def sell(self, choice):
        if choice == self.house:
            self.__bank_account.increase_money(House.PRICE)
            self.house = None
            print('Your house is sold')
        elif choice == self.car:
            self.__bank_account.increase_money(Car.PRICE)
            self.car = None
            print('Your car is sold')
        else:
            print('You dont have that to sell')
