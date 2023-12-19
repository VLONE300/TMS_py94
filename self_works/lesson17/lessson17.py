# create user vlone with password 'qwerty1234';
# GRANT ALL PRIVILEGES ON DATABASE psycopg2_lesson17 TO vlone;
# GRANT ALL PRIVILEGES ON SCHEMA public TO vlone;

import psycopg2
from config import host, user, db_name, password, port

connection = None
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
                id serial PRIMARY KEY,
                name varchar(50) NOT NULL )"""
        )
        print('table created')

except Exception as ex:
    print(f'Error while working {ex}')
finally:
    if connection:
        connection.close()
        print('connection closed')
