rows = int(input())

matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

flattened_matrix = [num for substring in matrix for num in substring]

print(flattened_matrix)
