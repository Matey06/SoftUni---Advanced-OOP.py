from project import dvd
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str | None:
        curr_customer = next((c for c in self.customers if c.id == customer_id), None)
        curr_dvd = next((d for d in self.dvds if d.id == dvd_id), None)
        if curr_customer and curr_dvd:
            if curr_dvd in curr_customer.rented_dvds:
                return f"{curr_customer.name} has already rented {curr_dvd.name}"
            elif curr_dvd.is_rented:
                return "DVD is already rented"
            elif curr_customer.age < curr_dvd.age_restriction:
                return  f"{curr_customer.name} should be at least {curr_dvd.age_restriction} to rent this movie"
            else:
                curr_dvd.is_rented = True
                curr_customer.rented_dvds.append(curr_dvd)
                return f"{curr_customer.name} has successfully rented {curr_dvd.name}"
        return None

    def return_dvd(self, customer_id: int, dvd_id: int) -> str | None:
        curr_customer = next((c for c in self.customers if c.id == customer_id), None)
        curr_dvd = next((d for d in self.dvds if d.id == dvd_id), None)
        if curr_customer and curr_dvd:
            if curr_dvd in curr_customer.rented_dvds:
                curr_dvd.is_rented = False
                curr_customer.rented_dvds.remove(curr_dvd)
                return f"{curr_customer.name} has successfully returned {curr_dvd.name}"
            return f"{curr_customer.name} does not have that DVD"
        return None

    def __repr__(self) -> str:
        result = []
        for customer in (self.customers):
            result.append(repr(customer))

        for dvd in (self.dvds):
            result.append(repr(dvd))

        return '\n'.join(result)

