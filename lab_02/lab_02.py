import csv
from sys import argv

FIELDS = ["name", "phone", "email", "group"]

students = []


def loadFromCsv(fileName):
    result = []
    with open(fileName, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            result.append({"name": row["name"], "phone": row["phone"], "email": row["email"], "group": row["group"]})
    result.sort(key=lambda item: item["name"])
    return result


def saveToCsv(fileName, data):
    with open(fileName, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        for item in data:
            writer.writerow(item)


def findInsertPosition(data, name):
    position = 0
    for item in data:
        if name > item["name"]:
            position += 1
        else:
            break
    return position


def findByName(data, name):
    for index, item in enumerate(data):
        if item["name"] == name:
            return index
    return -1


def addStudent(data, student):
    data.insert(findInsertPosition(data, student["name"]), student)


def deleteStudent(data, name):
    position = findByName(data, name)
    if position == -1:
        return False
    del data[position]
    return True


def updateStudent(data, name, newStudent):
    position = findByName(data, name)
    if position == -1:
        return False
    del data[position]
    addStudent(data, newStudent)
    return True


def printAllList():
    for elem in students:
        print("Студент: ім'я - " + elem["name"] + ", телефон - " + elem["phone"] + ", пошта - " + elem["email"] + ", група - " + elem["group"])


def addNewElement():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон студента: ")
    email = input("Введіть пошту студента: ")
    group = input("Введіть групу студента: ")
    addStudent(students, {"name": name, "phone": phone, "email": email, "group": group})
    print("Новий запис додано")


def deleteElement():
    name = input("Введіть ім'я для видалення: ")
    if deleteStudent(students, name):
        print("Запис видалено")
    else:
        print("Запис не знайдено")


def updateElement():
    name = input("Введіть ім'я для зміни: ")
    position = findByName(students, name)
    if position == -1:
        print("Запис не знайдено")
        return
    oldItem = students[position]
    print("Натисніть Enter, щоб залишити поточне значення")
    newName = input("Нове ім'я (" + oldItem["name"] + "): ") or oldItem["name"]
    newPhone = input("Новий телефон (" + oldItem["phone"] + "): ") or oldItem["phone"]
    newEmail = input("Нова пошта (" + oldItem["email"] + "): ") or oldItem["email"]
    newGroup = input("Нова група (" + oldItem["group"] + "): ") or oldItem["group"]
    updateStudent(students, name, {"name": newName, "phone": newPhone, "email": newEmail, "group": newGroup})
    print("Запис змінено")


def main():
    if len(argv) < 2:
        print("Використання: python lab_02.py файл.csv")
        return
    fileName = argv[1]
    try:
        students.extend(loadFromCsv(fileName))
        print("Завантажено студентів: " + str(len(students)) + " з " + fileName)
    except FileNotFoundError:
        print("Файл " + fileName + " не знайдено, список порожній")

    while True:
        choice = input("Оберіть дію [ C додати, U змінити, D видалити, P друк, X вихід ] ")
        match choice:
            case "C" | "c":
                addNewElement()
                printAllList()
            case "U" | "u":
                updateElement()
                printAllList()
            case "D" | "d":
                deleteElement()
            case "P" | "p":
                printAllList()
            case "X" | "x":
                saveToCsv(fileName, students)
                print("Дані збережено у " + fileName)
                break
            case _:
                print("Невірний вибір")


if __name__ == "__main__":
    main()
