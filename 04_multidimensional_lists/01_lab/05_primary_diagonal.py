rows = int(input())

square_matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split()]
    square_matrix.append(data)

primary_diagonal_sum = 0

for cur_row in range(rows):
    for cur_col in range(rows):
        if cur_col == cur_row:
            primary_diagonal_sum += square_matrix[cur_row][cur_col]


print(primary_diagonal_sum)
