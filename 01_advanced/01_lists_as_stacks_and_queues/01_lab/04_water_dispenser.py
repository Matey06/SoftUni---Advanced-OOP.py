from collections import deque

total_liters_of_water = int(input())
queue_for_water = deque()

while True:
    person = input()
    if person == 'Start':
        break
    queue_for_water.append(person)

while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill'):
        _, liters = command.split()
        total_liters_of_water += int(liters)
    elif command.isdigit():
        liters = int(command)
        if liters <= total_liters_of_water:
            total_liters_of_water -= liters
            print(f'{queue_for_water.popleft()} got water')
        else:
            print(f'{queue_for_water.popleft()} must wait')

print(f'{total_liters_of_water} liters left')
