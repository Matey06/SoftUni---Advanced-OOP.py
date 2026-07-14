from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: list[Room] = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int) -> "Hotel":
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        r = next((r for r in self.rooms if r.number == room_number), None)
        if r:
            return r.take_room(people)
        return None

    def free_room(self, room_number: int):
        r = next((r for r in self.rooms if r.number == room_number), None)
        if r:
            return r.free_room()
        return None

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if r.is_taken is False]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken is True]

        return "\n".join([
            f"Hotel {self.name} has {self.guests} total guests",
            f"Free rooms: {', '.join(free_rooms)}",
            f"Taken rooms: {', '.join(taken_rooms)}"
        ])