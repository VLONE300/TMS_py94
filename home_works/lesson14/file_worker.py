from home_works.lesson14.handlers import JsonHandler, TxtHandler
import os


class FileWorker:
    def __init__(self, path):
        self.path = path
        self.handler = None
        if self.get_file_extension() == '.json':
            self.handler = JsonHandler(self.path)
        elif self.get_file_extension() == '.txt':
            self.handler = TxtHandler(self.path)

    def get_file_extension(self):
        file_name, file_extension = os.path.splitext(self.path)
        return file_extension

    def read(self):
        return self.handler.read()

    def append(self, data):
        return self.handler.append(data)

    def close(self):
        return self.handler.close()
