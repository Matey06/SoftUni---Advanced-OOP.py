r, c = map(int, input().split())

matrix = [input().split() for _ in range(r)]

while True:
    line = input()
    if line == "END":
        break

    line = line.split()
    if len(line) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = int(line[1]), int(line[2]), int(line[3]), int(line[4])
    if ((line[0] == "swap"
            and 0 <= row1 < r
            and 0 <= col1 < c)
            and 0 <= row2 < r
            and 0 <= col2 < c):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")
