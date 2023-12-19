class User:
    def __init__(self, id, name, email, age):
        self._id = id
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f'{self.name}'
