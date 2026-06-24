algebraic_expression = input()

my_stack = []

for index in range(len(algebraic_expression)):
    if algebraic_expression[index] == "(":
        my_stack.append(index)
    elif algebraic_expression[index] == ")":
        start = my_stack.pop()
        end = index + 1
        print(algebraic_expression[start:end])
