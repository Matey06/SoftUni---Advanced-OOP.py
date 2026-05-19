unique_chemical_compounds = set()

for _ in range(int(input())):
    elements = input().split()
    for element in elements:
        unique_chemical_compounds.add(element)

print(*unique_chemical_compounds, sep='\n')
