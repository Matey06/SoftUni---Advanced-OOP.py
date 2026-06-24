rows = int(input())

matrix = []

for _ in range(rows):
    data = list(input())
    matrix.append(data)


symbol = input()

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            exit()

print(f"{symbol} does not occur in the matrix")
