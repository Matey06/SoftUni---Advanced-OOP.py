text = input()

try:
    repetition = int(input())
except ValueError as err:
    print(f"Variable times must be an integer!")
    print(f"{err} -> Original Error Message.")
else:
    print(text * repetition)