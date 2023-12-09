import json


class BaseHandler:
    def __init__(self, path):
        self.path = path
        self._file = None

    def read(self):
        raise NotImplementedError()

    def append(self, data):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class JsonHandler(BaseHandler):
    def read(self):
        with open(self.path) as file:
            content = file.read()
        return content

    def append(self, data):
        try:
            with open(self.path) as file:
                self._file = json.load(file)
        except (json.JSONDecodeError, ValueError):
            self._file = []

        self._file.append(data)
        with open(self.path, 'w') as file:
            json.dump(self._file, file)

    def close(self):
        pass


class TxtHandler(BaseHandler):

    def read(self):
        self._file = open(self.path, 'r')
        content = self._file.read()
        return content

    def append(self, data):
        with open(self.path, 'a') as file:
            file.write(data)

    def close(self):
        self._file.close()
