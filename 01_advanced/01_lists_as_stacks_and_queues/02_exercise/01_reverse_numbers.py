numbers_as_a_stack = [int(x) for x in input().split()]
reversed_numbers_as_a_stack = []

while numbers_as_a_stack:
    reversed_numbers_as_a_stack.append(numbers_as_a_stack.pop())

print(*reversed_numbers_as_a_stack)
