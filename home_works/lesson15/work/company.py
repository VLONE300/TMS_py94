from home_works.lesson15.bank_account import BankAccount


class Company:
    def __init__(self, name, profit, salary, legal_number):
        if profit <= salary:
            raise ValueError('...')
        self.name = name
        self.legal_number = legal_number
        self.__bank_account = BankAccount(f'{self.legal_number}_COMPANY')
        self.__profit = profit
        self.__salary = salary
        self.staff = set()

    def make_offer(self, human):
        human.company = self
        self.staff.add(human)

    def increase_money(self):
        clean_profit = self.__profit - self.__salary
        self.__bank_account.increase_money(clean_profit)
        return self.__salary

    def __str__(self):
        return f'{self.name}'
