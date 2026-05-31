from collections import deque

pumps_num = int(input())
pumps = deque()

stops = 0
start_position = 0

for i in range(pumps_num):
    litres_petrol, distance = map(int, input().split())
    pumps.append((litres_petrol, distance))


while stops < pumps_num:
    curr_fuel = 0
    for i in range(pumps_num):
        curr_fuel += pumps[i][0]
        if curr_fuel >= pumps[i][1]:
            stops += 1
            curr_fuel -= pumps[i][1]
        else:
            stops = 0
            pumps.rotate(-1)
            start_position += 1
            break

print(start_position)
