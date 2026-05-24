n = int(input())
matrix = [[int(x) for x in input().split(", ")]for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][-1-row])

print(f"Primary diagonal: {', '.join((map(str, primary_diagonal)))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join((map(str, secondary_diagonal)))}. Sum: {sum(secondary_diagonal)}")
