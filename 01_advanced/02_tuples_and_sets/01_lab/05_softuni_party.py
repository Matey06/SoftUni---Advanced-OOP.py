number_of_guests = int(input())
guests = set()

for _ in range(number_of_guests):
    reservation = input()
    guests.add(reservation)

while True:
    going_to_party = input()
    if going_to_party == "END":
        break

    guests.discard(going_to_party)

print(f'{len(guests)}')
sorted_guests = sorted(guests)
for person in sorted_guests:
    print(person)
