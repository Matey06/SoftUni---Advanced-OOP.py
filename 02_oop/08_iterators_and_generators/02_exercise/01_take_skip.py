class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.count:
            return self.i * self.step
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print("========================")
numbers = take_skip(10, 5)
for number in numbers:
 print(number)