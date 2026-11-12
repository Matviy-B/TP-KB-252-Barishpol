students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "KB-221"},
    {"name": "Emma", "phone": "0671234567", "email": "emma@gmail.com", "group": "KB-221"},
    {"name": "Jon", "phone": "0501234567", "email": "jon@gmail.com", "group": "KB-222"},
    {"name": "Zak", "phone": "0931234567", "email": "zak@gmail.com", "group": "KB-222"}
]


def printAllList():
    for elem in students:
        strForPrint = "Студент: ім'я - " + elem["name"] + ", телефон - " + elem["phone"] + ", пошта - " + elem["email"] + ", група - " + elem["group"]
        print(strForPrint)


def findInsertPosition(name):
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    return insertPosition


def addNewElement():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон студента: ")
    email = input("Введіть пошту студента: ")
    group = input("Введіть групу студента: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    students.insert(findInsertPosition(name), newItem)
    print("Новий запис додано")


def deleteElement():
    name = input("Введіть ім'я для видалення: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Запис не знайдено")
    else:
        print("Позиція видалення: " + str(deletePosition))
        del students[deletePosition]


def updateElement():
    name = input("Введіть ім'я для зміни: ")
    updatePosition = -1
    for item in students:
        if name == item["name"]:
            updatePosition = students.index(item)
            break
    if updatePosition == -1:
        print("Запис не знайдено")
        return
    oldItem = students.pop(updatePosition)
    print("Натисніть Enter, щоб залишити поточне значення")
    newName = input("Нове ім'я (" + oldItem["name"] + "): ") or oldItem["name"]
    newPhone = input("Новий телефон (" + oldItem["phone"] + "): ") or oldItem["phone"]
    newEmail = input("Нова пошта (" + oldItem["email"] + "): ") or oldItem["email"]
    newGroup = input("Нова група (" + oldItem["group"] + "): ") or oldItem["group"]
    newItem = {"name": newName, "phone": newPhone, "email": newEmail, "group": newGroup}
    students.insert(findInsertPosition(newName), newItem)
    print("Запис змінено")


def main():
    while True:
        choice = input("Оберіть дію [ C додати, U змінити, D видалити, P друк, X вихід ] ")
        match choice:
            case "C" | "c":
                print("Буде створено новий запис:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Запис буде змінено")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Запис буде видалено")
                deleteElement()
            case "P" | "p":
                print("Список буде надруковано")
                printAllList()
            case "X" | "x":
                print("Вихід")
                break
            case _:
                print("Невірний вибір")


main()
