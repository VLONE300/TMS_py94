class Car:
    PRICE = 40

    def __init__(self, brand, mark):
        self.brand = brand
        self.mark = mark

    def __str__(self):
        return f'{self.brand} - {self.mark}'
