def logged(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        name = function.__name__
        final_answer = f"you called {name}({', '.join(map(str, args))})\nit returned {result}"
        return final_answer

    return wrapper



@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
