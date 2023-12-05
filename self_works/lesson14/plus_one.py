def plus_one(digits: list):
    return [int(i) for i in str(int(''.join(map(str, digits))) + 1)]


print(plus_one([1, 2, 3]))
