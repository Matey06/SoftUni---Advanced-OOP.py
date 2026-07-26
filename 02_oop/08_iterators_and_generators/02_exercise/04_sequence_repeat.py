class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.number:
            index = self.i % len(self.sequence)
            return self.sequence[index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
print()
print("=====================")
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')