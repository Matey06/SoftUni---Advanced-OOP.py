from collections import deque

bees = deque(int(x) for x in input().split())
nectar_stack = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
}

while bees and nectar_stack:
    bee = bees[0]
    nectar = nectar_stack[-1]
    if bee <= nectar:
        total_honey += abs(operations[symbols[0]](bee, nectar))
        symbols.popleft()
        bees.popleft()
        nectar_stack.pop()
    else:
        nectar_stack.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar_stack:
    print(f"Nectar left: {', '.join(map(str, nectar_stack))}")
