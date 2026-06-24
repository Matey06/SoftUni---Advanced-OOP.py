import re

words = None

with open("words.txt") as f:
    words = f.read().split()

with open("input.txt") as file:
    text = file.read()

data = {}

for word in words:
    pattern = rf"\b{word}\b"
    matches = re.findall(pattern, text, re.IGNORECASE)
    data[word] = len(matches)

with open("output.txt", "w") as file:
    for word, repetition in sorted(data.items(), key=lambda x: -x[1]):
        file.write(f"{word} - {repetition}\n")