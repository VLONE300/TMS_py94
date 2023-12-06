class Price:

    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number


class DiscountPrice(Price):

    def __init__(self, number, discount):
        self.discount = discount
        super().__init__(number)

    def get_number(self):
        cost = super().get_number() * self.discount
        return cost


q = DiscountPrice(12, 0.5)
