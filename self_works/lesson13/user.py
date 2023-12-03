from custom_exceptions import NameError


class User:
    def __init__(self, name):
        self.name = name
        if not isinstance(self.name, str) or ' ' in self.name:
            raise NameError(f'Wrong {self.name}')


petya = User(1221424)
