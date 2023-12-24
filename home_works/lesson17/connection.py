import psycopg2
from config import host, user, db_name, password, port
from data_request import insert_product, insert_user, insert_food_intake

connection = None


def connection_to_db():
    global connection
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
            user_id = insert_user(cursor)
            product_id = insert_product(cursor)
            insert_food_intake(cursor, user_id, product_id)

    except Exception as ex:
        print(f'Error while working {ex}')
    finally:
        if connection:
            connection.close()
            print('connection closed')


connection_to_db()
