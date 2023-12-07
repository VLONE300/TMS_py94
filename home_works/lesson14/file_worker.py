from home_works.lesson14.handlers import JsonHandler, TxtHandler


class FileWorker:
    def __init__(self, path):
        self.path = path
        self.handler = None
        if '.json' in self.path:
            self.handler = JsonHandler()
        elif '.txt' in self.path:
            self.handler = TxtHandler()


q = FileWorker('qwerty.json')
