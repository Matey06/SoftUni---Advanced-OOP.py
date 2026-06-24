even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    name = list(input())
    for i in range(len(name)):
        name[i] = ord(name[i])

    result = (sum(name) // row)

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

even_sum = sum(even_set)
odd_sum = sum(odd_set)

if even_sum == odd_sum:
    print(*even_set.union(odd_set), sep=', ')
elif even_sum > odd_sum:
    print(*even_set.symmetric_difference(odd_set), sep=', ')
else:
    pass
    print(*odd_set.difference(even_set), sep=', ')
