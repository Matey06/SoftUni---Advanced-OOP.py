def finding_position(mat, ship_r, ship_c, r, c):
    updated_ship_row = None
    updated_ship_col = None
    if ship_r + r == len(matrix):
        updated_ship_row = 0
    elif ship_r + r < 0:
        updated_ship_row = len(matrix) - 1
    else:
        updated_ship_row = ship_r + r

    if ship_c + c == len(matrix):
        updated_ship_col = 0
    elif ship_c + c < 0:
        updated_ship_col = len(matrix) - 1
    else:
        updated_ship_col = ship_c + c

    return updated_ship_row, updated_ship_col


# First we create the input data
n = int(input()) # Size of the grid

matrix = [[el for el in input()] for _ in range(n)]

moves = {
    "up": (-1, 0),
    "down": (1 , 0),
    "left": (0, -1),
    "right": (0, 1)
}

# We count the treasures and find the ships position
treasures = 0
durability = 100
restored_durability = False
ship_row, ship_col = 0, 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "*":
            treasures += 1
        elif matrix[row][col] == "S":
            ship_row = row
            ship_col = col
            matrix[row][col] = "."

# Now is the time to create the main logic
while True:
    command = input()
    if command == "stop":
        print("Retreat! Some treasures remain unclaimed.")
        break

    row, col = moves[command][0], moves[command][1]

    ship_row, ship_col = finding_position(matrix, ship_row, ship_col, row, col)

    current_place_on_the_matrix = matrix[ship_row][ship_col]

    if current_place_on_the_matrix == "C":
        matrix[ship_row][ship_col] = "."
        if not restored_durability:
            restored_durability = True
            if durability + 25 <= 100:
                durability += 25
            else:
                durability = 100
    elif current_place_on_the_matrix == "*":
        treasures -= 1
        matrix[ship_row][ship_col] = "."
        if treasures == 0:
            print("Yo-ho-ho! All treasure chests collected!")
            break
    elif current_place_on_the_matrix == "M":
        durability -= 25
        matrix[ship_row][ship_col] = "."
        if durability <= 0:
            print(f"Shipwreck! Last known coordinates ({ship_row}, {ship_col})")
            break


# Lastly we print the final look of the matrix
print(f"Ship Durability: {durability}")

if treasures > 0:
    print(f"Unclaimed chests: {treasures}")

matrix[ship_row][ship_col] = "S"
[print(''.join(row)) for row in matrix]
