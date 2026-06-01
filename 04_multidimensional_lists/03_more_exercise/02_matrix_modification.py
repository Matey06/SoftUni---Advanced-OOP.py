n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    command = input().split()
    if command[0] == "END":
        [print(*row, end="\n") for row in matrix]
        break

    if command[0] == "Add":
        row, col, val = int(command[1]), int(command[2]), int(command[3])
        if 0 <= row < n and 0 <= col < n:
            matrix[row][col] += val
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        row, col, val = int(command[1]), int(command[2]), int(command[3])
        if 0 <= row < n and 0 <= col < n:
            matrix[row][col] -= val
        else:
            print("Invalid coordinates")
