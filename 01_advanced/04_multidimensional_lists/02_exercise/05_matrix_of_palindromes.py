r, c = map(int, input().split())
start_char = ord("a")

matrix = [[f"{chr(start_char + row)}{chr(start_char + row + col)}{chr(start_char + row)}" for col in range(c)] for row in range(r)]

[print(*row) for row in matrix]
