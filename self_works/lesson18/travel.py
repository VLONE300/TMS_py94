import requests
import json

from self_works.lesson18.user import User

urls = 'http://185.225.232.111:8000/user/'

users = requests.get(urls).json()
user_ids = [i['id'] for i in users]


user_inst = []
for user_id in user_ids:
    user_json = requests.get(f'{urls}{user_id}/').json()
    user_inst.append(
        User(**user_json)
    )
print(user_inst)

