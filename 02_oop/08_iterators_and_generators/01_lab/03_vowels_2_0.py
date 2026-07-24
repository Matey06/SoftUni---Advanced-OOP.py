class vowels:
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, text):
        self.text = text
        self.index = -1
        self.vowels_list = [el for el in self.text if el.lower() in vowels.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.vowels_list):
            return self.vowels_list[self.index]
        else:
            raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
