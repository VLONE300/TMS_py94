# # class Example:
# #     @staticmethod
# #     def hello():
# #         print('hello')
# #
# #     def hello2(self):
# #         print('hello2')
# import json
#
#
# class Example:
#     @classmethod
#     def class_hello(cls):
#         return f'class_hello{cls}'
#
#
# print(Example.class_hello())
#
# qw = Example()
# print(qw.class_hello())
import json

from self_works.lesson13.custom_exceptions import ConnectionRefused


class DataStorage:
    def __init__(self, file=None):
        self.file = file



    def connect_or_create(self, path):
        try:
            with open(path, 'r') as file:
                json.load(path)
                self.file = file
        except FileNotFoundError:
            with open('test.json', 'w') as file:
                json.dump('111',file)
                self.file = file

    def read(self):
        if self.file:
            return self.file.read()
        raise ConnectionRefused('error')






q = DataStorage()
q.connect_or_create('self_works/lesson13/test.json')
