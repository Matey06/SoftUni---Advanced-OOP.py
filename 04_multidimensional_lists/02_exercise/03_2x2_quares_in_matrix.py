r, c = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(r)]

identical_chars_count_2x2 = 0

for row in range(r - 1):
    for col in range(c - 1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            identical_chars_count_2x2 += 1

print(identical_chars_count_2x2)
