from random import randint


class Human:
    def __init__(self):
        self._bank_account = 0
        self.house = None
        self.car = None

    def check_bank_account(self):
        print(f'your account balance is {self._bank_account}')

    def work(self):
        salary = randint(5, 10)
        self._bank_account += salary
        print(f"you've earned {salary}")

    def buy(self):
        choice = input('What u want to buy 1-House/2-Car: ')
        if choice == '1':
            return self.house_purchase_permit()
        elif choice == '2':
            return self.car_purchase_permit()
        else:
            print('You cant buy this')

    def house_purchase_permit(self):
        if self.car:
            if self._bank_account >= 100:
                self._bank_account -= 100
                self.house = True
                print("you've successfully purchased a home")
            else:
                print(f'not enough money to buy a house {self._bank_account}/100')
        else:
            print('First u need to buy a car')

    def car_purchase_permit(self):
        if self._bank_account >= 40:
            self._bank_account -= 40
            self.car = True
            print("you've successfully purchased a car")
        else:
            print(f'not enough money to buy a house {self._bank_account}/40')

    def sell(self):
        choice = input('What u want to sell 1-House/2-Car: ')
        if choice == '1':
            self._bank_account += 100
            self.house = None
        elif choice == '2':
            self._bank_account += 40
            self.car = None
        else:
            print('You dont have that to sell')


man = Human()
man.check_bank_account()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.check_bank_account()
man.buy()
man.check_bank_account()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.work()
man.buy()
man.check_bank_account()
man.sell()
man.sell()
man.check_bank_account()
