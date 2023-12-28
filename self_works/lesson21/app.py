import requests
from self_works.lesson21.user import User


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

    def load_data_to_db(self, connection):
        cursor = connection.cursor()

        for user_id in self.get_users_id():
            user = self.get_user_data(user_id)

            cursor.execute(
                "INSERT INTO new_user (name, email, age) VALUES (%s, %s, %s);",
                (user.name, user.email, user.age))

        connection.commit()
