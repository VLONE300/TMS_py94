from custom_exceptions import ErrorName


class User:
    def __init__(self, name):
        self.name = name
        if not isinstance(self.name, str) or ' ' in self.name:
            raise ErrorName(f'Wrong {self.name}')


petya = User(1221424)
