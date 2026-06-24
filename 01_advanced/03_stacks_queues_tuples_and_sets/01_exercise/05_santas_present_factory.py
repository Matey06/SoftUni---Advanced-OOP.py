from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

toys = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_toys = {}

while magic and materials:
    total_magic_level = materials[-1] * magic[0]

    if total_magic_level < 0:
        materials.append(materials.pop() + magic.popleft())
    elif materials[-1] == 0 or magic[0] == 0:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()
    elif total_magic_level in toys:
        current_toy = toys[total_magic_level]
        if current_toy not in crafted_toys:
            crafted_toys[current_toy] = 0
        crafted_toys[current_toy] += 1
        magic.popleft()
        materials.pop()
    else:
        magic.popleft()
        materials[-1] += 15

if ("Doll" in crafted_toys.keys()
    and "Wooden train" in crafted_toys.keys()) or ("Teddy bear" in crafted_toys.keys()
                                                   and "Bicycle" in crafted_toys.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for key, value in sorted(crafted_toys.items()):
    print(f"{key}: {value}")
