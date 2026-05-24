rows, cols = map(int, input().split())
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_row = 0
max_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        total_sum = 0
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                total_sum += matrix[r][c]
        if total_sum > max_sum:
            max_sum = total_sum
            max_row = row
            max_col = col


sub_matrix = [[matrix[r][c] for c in range(max_col, max_col + 3)] for r in range(max_row, max_row + 3)]
print(f"Sum = {max_sum}")
[print(*row) for row in sub_matrix]
