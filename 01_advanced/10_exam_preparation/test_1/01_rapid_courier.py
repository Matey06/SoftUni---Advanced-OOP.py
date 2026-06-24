from collections import deque

# First we write the input data
packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())

total_weight_delivered = 0

# Secondly we write the logic of the program
while packages and couriers:
    curr_package = packages[-1]
    curr_courier = couriers[0]

    if curr_courier >= curr_package:
        total_weight_delivered += curr_package
        packages.pop()
        curr_courier -= 2 * curr_package
        if curr_courier > 0:
            couriers[0] = curr_courier
            couriers.rotate(-1)
        else:
            couriers.popleft()
    else:
        couriers.popleft()
        total_weight_delivered += curr_courier
        new_package_weight = curr_package - curr_courier
        packages[-1] = new_package_weight

# Printing the output of the program
print(f"Total weight: {total_weight_delivered} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

if packages and not couriers:
    print(f"Unfortunately, there are no more "
          f"available couriers to deliver the following packages: {', '.join(map(str, packages))}")

if couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")
