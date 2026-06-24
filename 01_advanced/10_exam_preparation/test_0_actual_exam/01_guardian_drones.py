from collections import deque

# First we create the input data
mechanical_parts = list(map(int, input().split()))
power_cells = deque(map(int, input().split()))

drones_to_assemble = {
    "Sentinel-X": 100,
    "Viper-MKII": 85,
    "Aegis-7": 75,
    "Striker-R": 65,
    "Titan-Core": 55
}

assembled_drones = []

# Secondly we build the main logic
while mechanical_parts and power_cells:
    if not drones_to_assemble:
        break

    curr_mechanical_part = mechanical_parts[-1]
    curr_power_cell = power_cells[0]

    activation_power = curr_mechanical_part + curr_power_cell

    if activation_power in drones_to_assemble.values():
        for drone, needed_power in drones_to_assemble.items():
            if drones_to_assemble[drone] == activation_power:
                assembled_drones.append(drone)
                del drones_to_assemble[drone]
                mechanical_parts.pop()
                power_cells.popleft()
                break
    elif activation_power > min(drones_to_assemble.values()):
        sorted_drones = dict(sorted(drones_to_assemble.items(), key=lambda x: -x[1]))
        for drone, needed_power in sorted_drones.items():
            if activation_power > needed_power:
                assembled_drones.append(drone)
                del drones_to_assemble[drone]
                mechanical_parts.pop()
                power_cells[0] = curr_power_cell - 30
                if power_cells[0] <= 0:
                    power_cells.popleft()
                    break
                else:
                    power_cells.rotate(-1)
                    break
    else:
        mechanical_parts.pop()
        power_cells[0] = curr_power_cell - 1
        if power_cells[0] <= 0:
            power_cells.popleft()
        else:
            power_cells.rotate(-1)


# Now we print the output
if not drones_to_assemble:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if assembled_drones:
    print(f"Assembled Drones: {', '.join(assembled_drones)}")

if mechanical_parts:
    reversed_mechanical_parts = list(map(str, reversed(mechanical_parts)))
    print(f"Mechanical Parts: {', '.join(reversed_mechanical_parts)}")

if power_cells:
    print(f"Power Cells: {', '.join(map(str, power_cells))}")
