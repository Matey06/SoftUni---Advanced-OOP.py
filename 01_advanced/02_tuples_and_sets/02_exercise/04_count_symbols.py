txt = input()

characters = set(txt)

for ch in sorted(characters):
    print(f'{ch}: {txt.count(ch)} time/s')
