class BaseHandler:
    def read(self):
        raise NotImplementedError()

    def append(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class JsonHandler(BaseHandler):

    def read(self):
        ...

    def append(self):
        ...

    def close(self):
        ...


class TxtHandler(BaseHandler):
    def read(self):
        ...

    def append(self):
        ...

    def close(self):
        ...
