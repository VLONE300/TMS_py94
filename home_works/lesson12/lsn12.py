class Moving:
    def move(self):
        raise NotImplementedError()


class Animal(Moving):
    def voice(self):
        raise NotImplementedError()


class Transport(Moving):

    def launch(self):
        raise NotImplementedError()


class Car(Transport):
    def __init__(self):
        self.status = 'not_started'

    def launch(self):
        self.status = 'started'
        return 'launch'

    def move(self):
        if self.status == 'started':
            return 'rides'
        return "car not started"


class Duck(Animal):
    def voice(self):
        return 'crya'

    def move(self):
        return "swim"


class Tiger(Animal):
    def voice(self):
        return 'arghh'

    def move(self):
        return 'run'


duck = Duck()
tiger = Tiger()
car = Car()

print(duck.move(), duck.voice())
print(tiger.move(), tiger.voice())
print(car.move(), car.launch(), car.status)
