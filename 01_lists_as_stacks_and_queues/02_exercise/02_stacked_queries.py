my_stack = []
n = int(input())

mapper = {
    "1": lambda i: my_stack.append(int(i)),
    "2": lambda: my_stack.pop() if my_stack else None,
    "3": lambda: print(max(my_stack)) if my_stack else None,
    "4": lambda: print(min(my_stack)) if my_stack else None,
}

for _ in range(n):
    command = input().split()
    func = mapper[command[0]](*command[1:])


print(*reversed(my_stack), sep=", ")
