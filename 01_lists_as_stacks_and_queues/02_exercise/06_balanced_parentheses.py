parentheses = list(input())
stack = []

dict_parentheses = {
    "(": ")",
    "[": "]",
    "{": "}"
}

balanced = True

for el in parentheses:
    if el in dict_parentheses:
        stack.append(el)
    elif el in dict_parentheses.values():
        if not stack or dict_parentheses[stack[-1]] != el:
            balanced = False
            break
        else:
            stack.pop()


if not stack and balanced:
    print("YES")
else:
    print("NO")
