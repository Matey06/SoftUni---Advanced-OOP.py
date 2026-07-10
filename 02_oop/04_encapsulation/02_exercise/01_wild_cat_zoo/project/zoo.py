from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if price > self.__budget:
            return f"Not enough budget"
        if len(self.animals) >= self.__animal_capacity:
            return f"Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"


    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        worker = next((w for w in self.workers if worker_name == w.name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        all_salaries_sum = (sum(w.salary for w in self.workers))
        if all_salaries_sum <= self.__budget:
            self.__budget -= all_salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_amount_for_animal_care = (sum(a.money_for_care for a in self.animals))
        if total_amount_for_animal_care <= self.__budget:
            self.__budget -= total_amount_for_animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount) -> None:
        self.__budget += amount

    def animals_status(self):
        lions_num = []
        tigers_num = []
        cheetahs_num = []

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions_num.append(animal.__repr__())
            elif animal.__class__.__name__ == "Tiger":
                tigers_num.append(animal.__repr__())
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs_num.append(animal.__repr__())

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions_num)} Lions:",
        ]

        for l in lions_num:
            result.append(l)

        result.append(f"----- {len(tigers_num)} Tigers:")
        for t in tigers_num:
            result.append(t)

        result.append(f"----- {len(cheetahs_num)} Cheetahs:")
        for c in cheetahs_num:
            result.append(c)

        return '\n'.join(result)

    def workers_status(self):
        keepers_num = []
        caretakers_num = []
        vets_num = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers_num.append(worker.__repr__())
            elif worker.__class__.__name__ == "Caretaker":
                caretakers_num.append(worker.__repr__())
            elif worker.__class__.__name__ == "Vet":
                vets_num.append(worker.__repr__())

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(keepers_num)} Keepers:",
        ]

        for k in keepers_num:
            result.append(k)

        result.append(f"----- {len(caretakers_num)} Caretakers:")
        for c in caretakers_num:
            result.append(c)

        result.append(f"----- {len(vets_num)} Vets:")
        for v in vets_num:
            result.append(v)

        return '\n'.join(result)


