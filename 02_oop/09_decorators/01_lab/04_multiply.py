def multiply(n):
    def decorator(function):
        def wrapper(*args, **kwargs):
            data = function(*args, **kwargs)
            return data * n
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10
print(add_ten(3))