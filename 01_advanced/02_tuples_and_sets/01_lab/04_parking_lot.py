n = int(input())
parking_lot = set()

for _ in range(n):
    action, number  = input().split(', ')
    if action == "IN":
        parking_lot.add(number)
    elif action == "OUT":
        parking_lot.discard(number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")
