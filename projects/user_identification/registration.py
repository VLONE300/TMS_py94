import json

from validators import uniqueness_check


def new_entry(email, password, users):
    users.append({'email': email, 'password': password})
    json.dump(users, open('users.json', 'w'))


def sign_in(users):
    while True:
        email = input('Enter a name for the mailbox: ')
        if uniqueness_check(email, users):
            print('Such a mailbox already exists')
            continue
        break

    while True:
        password = input('Enter your password: ')
        repeat_password = input('Repeat the password: ')
        if password == repeat_password:
            break
        else:
            print("The passwords don't match")

    new_entry(email, password, users)
    return 'You have successfully registered'
