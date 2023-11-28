class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def gp(self):
        print(f'i am {self.name}, im going!. Im {self.age} years')


Fedya = Person('Fedya', 20)
Mitya = Person('Mitya', 18)
Vasya = Person('Vasya', 9)

Fedya.gp()
Mitya.gp()
Vasya.gp()
