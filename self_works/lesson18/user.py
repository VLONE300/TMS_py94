class User:
    def __init__(self, id, name, email, age):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)
