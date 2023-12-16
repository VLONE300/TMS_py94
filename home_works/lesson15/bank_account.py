class BankAccount:
    created_accounts = set()

    def __init__(self, num):
        self.bank_acc_number = f'{num}__bank_account'
        if self.bank_acc_number in self.created_accounts:
            raise ValueError('Already in bank system')

        self.__amount = 0

    @property
    def amount(self):
        return self.__amount

    def __str__(self):
        return f'{self.amount}'

    def increase_money(self, amount):
        self.__amount += amount

    def decrease_money(self, amount):
        self.__amount -= amount
