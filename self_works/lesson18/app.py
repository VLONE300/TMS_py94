import psycopg2
from data_loader import DataLoader
from config import host, user, password, db_name, port


def main():
    base_url = 'http://185.225.232.111:8000'
    data_loader = DataLoader(base_url)

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )

    data_loader.load_data_to_db(connection)

    connection.close()


if __name__ == "__main__":
    main()
