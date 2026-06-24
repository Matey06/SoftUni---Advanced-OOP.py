def calculations(stars, size):
    print((" " * (size - stars)) + ("* " * stars))


def print_upper_part(size):
    for row in range(1, size + 1):
        calculations(row, size)


def print_bottom_part(size):
    for row in range(size - 1, 0, -1):
        calculations(row, size)


def print_rhombus(size):
    print_upper_part(size)
    print_bottom_part(size)


n = int(input())

print_rhombus(n)
