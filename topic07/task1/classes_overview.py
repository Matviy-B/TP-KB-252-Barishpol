class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


class Puppy(Dog):
    def add_trick(self, trick):
        super().add_trick(trick.upper())


rex = Dog("Rex")
tom = Puppy("Tom")

rex.add_trick("сидіти")
tom.add_trick("голос")

print("Змінна класу:", Dog.species, rex.species, tom.species)
print("Імена:", rex.name, tom.name)
print("Фокуси Rex:", rex.tricks)
print("Фокуси Tom:", tom.tricks)
print("Tom - це Dog?", isinstance(tom, Dog))
