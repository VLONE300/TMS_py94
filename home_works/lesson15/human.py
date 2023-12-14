# from random import randint

from home_works.lesson15.bank_account import BankAccount


class Human:
    created_passport_nums = set()

    def __init__(self, name, passport_id):
        if passport_id in self.created_passport_nums:
            raise ValueError('...')

        self.name = name
        self.passport_id = passport_id
        self.__bank_account = BankAccount(self.passport_id)
        self.company = None

    def __repr__(self):
        return f'{self.name, self.passport_id}'

    def work(self):
        if not self.company:
            print('go find a job')
            return

        salary = self.company.increase_money()
        self.__bank_account.increase_money(salary)

#     def check_bank_account(self):
#         print(f'your account balance is {self._bank_account}')
#
#     def work(self):
#         salary = randint(5, 10)
#         self._bank_account += salary
#         print(f"you've earned {salary}")
#
#     def buy(self):
#         choice = input('What u want to buy 1-House/2-Car: ')
#         if choice == '1':
#             return self.house_purchase_permit()
#         elif choice == '2':
#             return self.car_purchase_permit()
#         else:
#             print('You cant buy this')
#
#     def house_purchase_permit(self):
#         if self.car:
#             if self._bank_account >= 100:
#                 self._bank_account -= 100
#                 self.house = True
#                 print("you've successfully purchased a home")
#             else:
#                 print(f'not enough money to buy a house {self._bank_account}/100')
#         else:
#             print('First u need to buy a car')
#
#     def car_purchase_permit(self):
#         if self._bank_account >= 40:
#             self._bank_account -= 40
#             self.car = True
#             print("you've successfully purchased a car")
#         else:
#             print(f'not enough money to buy a house {self._bank_account}/40')
#
#     def sell(self):
#         choice = input('What u want to sell 1-House/2-Car: ')
#         if choice == '1':
#             self._bank_account += 100
#             self.house = None
#         elif choice == '2':
#             self._bank_account += 40
#             self.car = None
#         else:
#             print('You dont have that to sell')
#
#
# man = Human()
# man.check_bank_account()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.check_bank_account()
# man.buy()
# man.check_bank_account()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.work()
# man.buy()
# man.check_bank_account()
# man.sell()
# man.sell()
# man.check_bank_account()
