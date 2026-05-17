numbers = tuple([float(num) for num in input().split()])

occurrences = {}

for number in numbers:
    if number not in occurrences:
        occurrences[number] = numbers.count(number)

for key, value in occurrences.items():
    print(f'{key:.1f} - {value} times')
