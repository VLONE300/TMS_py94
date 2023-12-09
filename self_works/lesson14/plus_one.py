def plus_one(digits: list):
    return list(map(int, str(int(''.join(map(str, digits))) + 1)))


print(plus_one([4, 4, 3, 2]))
