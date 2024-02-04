import requests
from sqlalchemy.orm import Session
from self_works.lesson21.db import NewUser, engine

url = 'http://185.225.232.111:8000'


def get_users_id():
    users = requests.get(f'{url}/user/').json()
    user_ids = [user['id'] for user in users]
    return user_ids


def get_user_data(user_id):
    user_data = requests.get(f'{url}/user/{user_id}/').json()
    return user_data


def get_email_from_db():
    emails = []
    with Session(autoflush=False, bind=engine) as db:
        for email in db.query(NewUser.email).all():
            emails.append(*email)
    return emails
