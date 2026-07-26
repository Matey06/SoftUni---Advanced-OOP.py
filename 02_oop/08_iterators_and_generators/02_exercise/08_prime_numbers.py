def get_primes(numbers):
    for num in numbers:
        if num < 2:
            continue
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))