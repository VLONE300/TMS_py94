import requests
from self_works.lesson18.country import Country
from self_works.lesson18.user import User


class DataLoader:
    def __init__(self, url):
        self.url = url

    def get_users_id(self):
        users = requests.get(f'{self.url}/user/').json()
        user_ids = [user['id'] for user in users]
        return user_ids

    def get_user_data(self, user_id):
        user_data = requests.get(f'{self.url}/user/{user_id}/').json()
        return User(**user_data)

    def get_countries_for_user(self, user_id):
        countries = requests.get(f'{self.url}/user/{user_id}/country/').json()
        return [Country(**country) for country in countries]

    def load_data_to_db(self, connection):
        cursor = connection.cursor()

        for user_id in self.get_users_id():
            user = self.get_user_data(user_id)
            user.countries = self.get_countries_for_user(user_id)

            cursor.execute(
                "INSERT INTO travel_user (foreign_id, name, email, age) VALUES (%s, %s, %s, %s) "
                "RETURNING id;",
                (user.id, user.name, user.email, user.age))
            user_db_id = cursor.fetchone()[0]

            for country in user.countries:

                cursor.execute(
                    "INSERT INTO travel_country (foreign_id, name) VALUES (%s, %s) ON CONFLICT "
                    "DO NOTHING RETURNING id;",
                    (country.id, country.name))
                country_db_id_result = cursor.fetchone()

                if country_db_id_result:
                    country_db_id = country_db_id_result[0]
                else:
                    cursor.execute(
                        "SELECT id FROM travel_country WHERE foreign_id = %s;", (country.id,))
                    country_db_id = cursor.fetchone()[0]
                cursor.execute("INSERT INTO usercountry (user_id, country_id) VALUES (%s, %s);",
                               (user_db_id, country_db_id))

        connection.commit()
