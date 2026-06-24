def math_operations(*args, **kwargs):
    for i in range(len(args)):
        for key, value in kwargs.items():
            current_key = i % 4
            if current_key == 0:
                if key == "a":
                    kwargs[key] = value + args[i]
            elif current_key == 1:
                if key == "s":
                    kwargs[key] = value - args[i]
            elif current_key == 2:
                if key == "d":
                    if value != 0 and args[i] != 0:
                        kwargs[key] = value / args[i]
            elif current_key == 3:
                if key == "m":
                    kwargs[key] = value * args[i]

    sorted_data = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = []
    for key, value in sorted_data:
        result.append(f"{key}: {value:.1f}")
    return "\n".join(result)

#Test cases
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
