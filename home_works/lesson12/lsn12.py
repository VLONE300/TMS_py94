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
    def __init__(self, not_started):
        self.started = not_started


    def launch(self):
        self.started = 'starteed'
        return 'launch'

    def move(self):
        return 'rides'




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
print(car.move(), car.launch(), )
