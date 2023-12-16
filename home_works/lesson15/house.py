class House:
    PRICE = 100

    def __init__(self, street):
        self.street = street

    def __str__(self):
        return f'The house on the street {self.street}'
