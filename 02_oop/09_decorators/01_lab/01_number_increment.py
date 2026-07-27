def number_increment(numbers):

    def increase():
        result = [element + 1 for element in numbers]

        return result

    return increase()

print(number_increment([1, 2, 3]))