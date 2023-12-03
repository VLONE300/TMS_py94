import json


class DataStorage:
    def __init__(self, path, status='disconnected', content=None):
        self._path = path
        self.status = status
        self.content = content
        self._file = None

    @property
    def path(self):
        return self._path

    def _create_storage(self):
        return open(self._path, 'w')

    def connect(self):
        if self.status == 'disconnected':
            try:
                self._file = open(self._path, 'r')
                self.status = 'connected'
                self.content = self._file.read()
            except FileNotFoundError:
                self._create_storage()
        return self._file

    def disconnect(self):
        if self.status == 'connected':
            self._file.close()
            self.status = 'disconnected'


class DataStorageWrite(DataStorage):
    def connect(self):
        if self.status == 'disconnected':
            try:
                self._file = open(self._path, 'a')
                self.status = 'connected'
            except FileNotFoundError:
                self._create_storage()
        return self._file

    def _create_storage(self):
        return open(self._path,'a')

    def append(self, string):
        with self.connect() as file:
            json.dump(string, file)
            self.disconnect()


