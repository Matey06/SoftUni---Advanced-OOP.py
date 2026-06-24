rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)


for cur_col in range(cols):
    colum_sum = 0
    for cur_row in range(rows):
        colum_sum += matrix[cur_row][cur_col]
    print(colum_sum)
