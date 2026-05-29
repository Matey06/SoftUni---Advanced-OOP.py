def sum_numbers(*args):
    p_sum = 0
    n_sum = 0
    for num in args:
        if num >= 0:
            p_sum += num
        else:
            n_sum += num

    return p_sum, n_sum


numbers = map(int, input().split())

positive_sum, negative_sum = sum_numbers(*numbers)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print(f"The negatives are stronger than the positives")
else:
    print(f"The positives are stronger than the negatives")
