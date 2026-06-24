numbers = input().split("|")
matrix = []

for el in numbers:
    matrix.append(el.split())

flattened_matrix = []
for el in reversed(matrix):
    if el:
        flattened_matrix.append(el)

[print(*row, end=" ") for row in flattened_matrix]
