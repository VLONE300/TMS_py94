import json
from self_works.lesson13.custom_exceptions import ConnectionRefused


class DataStorage:
    file = None

    @classmethod
    def connect_or_create(cls, path):
        try:
            cls.file = open(path, 'r+')
        except FileNotFoundError:
            cls.file = open(path, 'w')

    @classmethod
    def read(cls):
        if cls.file:
            return cls.file.read()
        raise ConnectionRefused('first you need to call the method connect_or_create')


DataStorage.connect_or_create('example.json')
data = DataStorage.read()
print(data)