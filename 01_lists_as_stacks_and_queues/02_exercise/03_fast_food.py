from collections import deque

prepared_food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    if  prepared_food >= orders[0]:
        served_order = orders.popleft()
        prepared_food -= served_order
    else:
        print(f"Orders left: {' '.join(map(str, orders))}")
        break
else:
    print("Orders complete")
