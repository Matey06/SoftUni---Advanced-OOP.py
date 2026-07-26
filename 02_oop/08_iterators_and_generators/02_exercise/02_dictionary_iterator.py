class dictionary_iter:
    def __init__(self, dictionary):
        self.dict_as_set_of_tuples = tuple(dictionary.items())
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self.dict_as_set_of_tuples):
            return self.dict_as_set_of_tuples[self.i]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
print("=======================")
result = dictionary_iter({"name": "Peter",
"age": 24})
for x in result:
    print(x)