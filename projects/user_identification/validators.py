def check_data(email, password, users):
    for i in users:
        if email == i["email"] and password == i["password"]:
            return f"Welcome {i['email']}"
    return 'Incorrect username or password'


def uniqueness_check(email, users):
    for i in users:
        if email == i['email']:
            return True
