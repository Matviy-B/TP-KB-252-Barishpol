class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} років"


students = [
    Student("Оксана", 20),
    Student("Андрій", 19),
    Student("Іван", 22),
    Student("Марія", 19),
    Student("Богдан", 21),
]

print("За іменем:")
for student in sorted(students, key=lambda s: s.name):
    print(student)

print("\nЗа віком:")
for student in sorted(students, key=lambda s: s.age):
    print(student)
