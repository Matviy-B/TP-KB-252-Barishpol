students = [
    {"name": "Оксана", "grade": 88},
    {"name": "Андрій", "grade": 95},
    {"name": "Іван", "grade": 72},
    {"name": "Марія", "grade": 91},
    {"name": "Богдан", "grade": 60},
]

print("Початковий список:")
for student in students:
    print(student)

print("\nЗа іменем:")
for student in sorted(students, key=lambda item: item["name"]):
    print(student)

print("\nЗа оцінкою (зростання):")
for student in sorted(students, key=lambda item: item["grade"]):
    print(student)

print("\nЗа оцінкою (спадання):")
for student in sorted(students, key=lambda item: item["grade"], reverse=True):
    print(student)
