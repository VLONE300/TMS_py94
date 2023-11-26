from random import randint


def get_random_numbers():
    while True:
        print('Диапазон должен включать минимум 5 и максимум 30 чисел.')
        start = int(input('Введите начало диапазона '))
        end = int(input('Введите конец диапазона '))
        if check_range(start, end):
            return [randint(start, end) for _ in range(3)]
        continue


def check_range(start, end):
    return 5 <= len(range(start, end)) <= 30


def input_user_number():
    usr_numbers = []
    while len(usr_numbers) < 3:
        number = input('Введите число: ')
        if number == 'exit':
            quit()
        elif int(number) in usr_numbers:
            print('Вы уже вводили это число: ')
            continue
        usr_numbers.append(int(number))
    return usr_numbers


def count_user_numbers(numbers, random_numbers):
    return len([i for i in numbers if i in random_numbers])


def game():
    range_numbers = get_random_numbers()
    while True:
        users_numbers = input_user_number()
        amount = count_user_numbers(users_numbers, range_numbers)
        print(f'Вы угадали {amount}/3 чисел')
        if amount == 3:
            return 'Ты выиграл'
        print('Попробуй еще раз')


print(game())
