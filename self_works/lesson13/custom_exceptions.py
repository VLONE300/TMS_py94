class ErrorName(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'name {self.name}'


class ConnectionRefused(Exception):
    ...
