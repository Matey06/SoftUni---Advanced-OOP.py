def even_parameters(function):
    def wrapper(*args, **kwargs):
        all_args_are_even_nums = True
        for el in args:
            if isinstance(el, int) and el % 2 == 0:
                continue
            else:
                all_args_are_even_nums = False

        if all_args_are_even_nums:
            return function(*args, **kwargs)
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

print("=========================")

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))