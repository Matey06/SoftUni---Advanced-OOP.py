number_of_guests = int(input())
guests = set()

for _ in range(number_of_guests):
    guests.add(input())

while True:
    going_to_party = input()
    if going_to_party == "END":
        break

    guests.discard(going_to_party)

not_partying = [person for person in guests]
not_partying.sort()

print(f'{len(not_partying)}')
for person in not_partying:
    print(person)
