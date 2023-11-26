from registration import sign_in
from entry import log_in
import json

users = json.load(open('users.json'))


def authentication():
    choice = input('Select the action 1-Entry / 2-Registration: ')
    if choice == '1':
        print(log_in(users))
    elif choice == '2':
        print(sign_in(users))


authentication()
