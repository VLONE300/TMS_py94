import time


def time_decorator(foo):
    def wrapper():
        start = time.monotonic()
        res = foo()
        end = time.monotonic()
        return res, f"{end - start} секунды"

    return wrapper


@time_decorator
def test():
    time.sleep(3)
    return 'Hello'


print(test())