from getters import get_email, get_password
from validators import check_data


def log_in(users):
    email = get_email()
    if email == 'exit':
        print('Bye')
        quit()
    password = get_password()
    return check_data(email=email, password=password, users=users)
