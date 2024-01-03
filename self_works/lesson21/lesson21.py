class PostgresDBMS:
    working = True


class AbstractManagerConnector:
    def __init__(self, host, port, ):
        self.host = host
        self.port = port

    def connect(self):
        raise NotImplementedError


class PGManagerConnector(AbstractManagerConnector):
    """
    Реализовать метод connect, не принимающий аргументов (как и в AbstractManagerConnector),
    в PGManagerConnector таким образом,
    что бы при его вызове, через экземпляр класса PGManagerConnector, мы получали надпись ->
    Connected to 127.0.0.1:5432 в том случае если аргумент working класса PostgresDBMS имеет значение True
    И получать надпись -> Connection refused если это значение равно False
    """

    def connect(self):
        if PostgresDBMS.working:
            print(f'Connected to {self.host}:{self.port}')
        else:
            print('Connection refused')


pg_connector = PGManagerConnector(host='127.0.0.1', port='5432')
pg_connector.connect()
