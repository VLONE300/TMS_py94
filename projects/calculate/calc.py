from custom_exeptions import UnknownOperation, InputNonDigit


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ZeroDivisionError("You can't divide by zero.")
    return x / y


def degree_conversion(x, y):
    return x ** y


def calculator():
    operations = {
        '+': plus,
        '-': minus,
        '*': multiply,
        '/': division,
        '**': degree_conversion
    }
    try:
        operation = input("Enter operation (+, -, *, /, **): ")

        if operation not in ('+', '-', '*', '/', '**'):
            raise UnknownOperation("Unknown operation entered.")

        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))

        if not isinstance(x, int) or not isinstance(y, int):
            raise InputNonDigit("Input must be numeric.")

        print(operations[operation](x, y))

    except UnknownOperation as Unknown:
        print(f"Error: {Unknown}")
    except InputNonDigit as NonDigit:
        print(f"Error: {NonDigit}")
    except ZeroDivisionError as ZeroDivision:
        print(f"Error: {ZeroDivision}")
