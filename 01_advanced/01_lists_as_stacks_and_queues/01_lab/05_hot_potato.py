from collections import deque

kids = deque(input().split())

n = int(input())

while len(kids) != 1:
    removed_kid = - (n - 1)
    kids.rotate(removed_kid)
    print(f'Removed {kids.popleft()}')


print(f'Last is {kids.pop()}')
