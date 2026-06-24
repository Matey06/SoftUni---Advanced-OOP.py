clothing = [int(x) for x in input().split()]
racks_capacity = int(input())

racks_used = 1
current_rack_sum = 0

while clothing:
    curr_clothing = clothing[-1]
    current_rack_sum += curr_clothing
    if current_rack_sum <= racks_capacity:
        clothing.pop()
    else:
        racks_used += 1
        current_rack_sum = 0


print(racks_used)
