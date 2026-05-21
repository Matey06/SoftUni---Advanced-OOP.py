rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)


max_sum = float("-inf")
sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current_num = matrix[row][col]
        next_num = matrix[row][col + 1]
        num_below = matrix[row + 1][col]
        diagonal_num = matrix[row + 1][col + 1]
        current_sum = current_num + next_num + num_below + diagonal_num
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_num, next_num], [num_below, diagonal_num]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
