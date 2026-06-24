def finding_position(mat, bee_r, bee_c, row, col):
    updated_bee_row = None
    updated_bee_col = None
    if bee_r + row == len(matrix):
        updated_bee_row = 0
    elif bee_r + row < 0:
        updated_bee_row = len(matrix) - 1
    else:
        updated_bee_row = bee_r + row

    if bee_c + col == len(matrix):
        updated_bee_col = 0
    elif bee_c + col < 0:
        updated_bee_col = len(matrix) - 1
    else:
        updated_bee_col = bee_c + col

    return updated_bee_row, updated_bee_col


# First we create the matrix
matrix = [[el for el in input()] for _ in range(int(input()))]

initial_energy = 15
nectar = 0

energy_restored = False

# Secondly we create a mapper for the possible moves and find the bee position
moves = {
    "up": (-1, 0),
    "down": (1 , 0),
    "left": (0, -1),
    "right": (0, 1)
}

bee_position = None

found_bee = False
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "B":
            bee_position = [row, col]
            found_bee = True
            break
    if found_bee:
        break

# Now we start the logic
while True:
    move = input()
    initial_energy -= 1
    bee_row = bee_position[0]
    bee_col = bee_position[1]

    matrix[bee_row][bee_col] = "-"

    r, c = moves[move]

    new_bee_row, new_bee_col = finding_position(matrix, bee_row, bee_col, r, c)

    # Now we check what we have on the current position
    current_element = matrix[new_bee_row][new_bee_col]

    if current_element.isdigit():
        nectar += int(current_element)
    elif current_element == "H":
        if nectar >= 30:
            #Before we break we need to change the bee position
            print(f"Great job, Beesy! The hive is full. Energy left: {initial_energy}")
            matrix[new_bee_row][new_bee_col] = "B"
            break
        else:
            #Before we break we need to change the bee position
            print(f"Beesy did not manage to collect enough nectar.")
            matrix[new_bee_row][new_bee_col] = "B"
            break

    matrix[new_bee_row][new_bee_col] = "B"
    bee_position[0] = new_bee_row
    bee_position[1] = new_bee_col

    if initial_energy == 0:
        if nectar >= 30 and not energy_restored:
            energy_restored = True
            initial_energy = nectar - 30
            nectar = 30

            if initial_energy == 0:
                print("This is the end! Beesy ran out of energy.")
                break
        else:
            print("This is the end! Beesy ran out of energy.")
            break

for row in matrix:
    print("".join(row))
