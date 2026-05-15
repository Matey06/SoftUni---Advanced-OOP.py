from collections import deque

people = deque()

while True:
    line = input()
    if line == "End":
        print(f'{len(people)} people remaining.')
        break
    elif line == "Paid":
        for _ in range(len(people)):
            print(people.popleft())
    else:
        people.append(line)
