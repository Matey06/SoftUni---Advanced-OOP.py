class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    try:
        number = int(input())
        if number < 0:
            raise ValueCannotBeNegative
    except ValueCannotBeNegative:
        print("Number cannot be negative!")
