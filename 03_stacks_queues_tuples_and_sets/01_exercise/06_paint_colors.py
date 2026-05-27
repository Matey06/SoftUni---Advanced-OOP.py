from collections import deque

main_colors = ("red", "yellow", "blue")
secondary_colors = {
    "orange": ("red", "yellow"),
    "purple": ("red", "blue"),
    "green": ("yellow", "blue"),
}

strings = deque(input().split())

collected_colors = []

while strings:
    first_string = strings.popleft()
    second_string = strings.pop() if strings else ""

    for color in (first_string + second_string, second_string + first_string):
        if color in main_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    else:
        index = len(strings) // 2

        modified_first_string = first_string[:-1]
        modified_second_string = second_string[:-1]

        if modified_second_string != "":
            strings.insert(index, modified_second_string)
        if modified_first_string != "":
            strings.insert(index, modified_first_string)

filtered_colors = []

for color in collected_colors:
    if color not in secondary_colors:
        filtered_colors.append(color)
    else:
        for col in secondary_colors[color]:
            if col not in collected_colors:
                break
        else:
            filtered_colors.append(color)

print(filtered_colors)
