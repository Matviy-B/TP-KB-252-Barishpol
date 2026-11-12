from sys import argv

from student import Student
from student_list import StudentList
from utils import Utils


def add_new_student(student_list):
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон студента: ")
    email = input("Введіть пошту студента: ")
    group = input("Введіть групу студента: ")
    student_list.add(Student(name, phone, email, group))
    print("Нового студента додано")


def delete_student(student_list):
    name = input("Введіть ім'я для видалення: ")
    if student_list.delete(name):
        print("Студента видалено")
    else:
        print("Студента не знайдено")


def update_student(student_list):
    name = input("Введіть ім'я для зміни: ")
    position = student_list.find_position(name)
    if position == -1:
        print("Студента не знайдено")
        return
    old = student_list.students[position]
    print("Натисніть Enter, щоб залишити поточне значення")
    new_name = input(f"Нове ім'я ({old.name}): ") or old.name
    new_phone = input(f"Новий телефон ({old.phone}): ") or old.phone
    new_email = input(f"Нова пошта ({old.email}): ") or old.email
    new_group = input(f"Нова група ({old.group}): ") or old.group
    student_list.update(name, Student(new_name, new_phone, new_email, new_group))
    print("Дані студента змінено")


def main():
    if len(argv) < 2:
        print("Використання: python lab_03.py файл.csv")
        return
    utils = Utils(argv[1])
    try:
        student_list = utils.load()
        print(f"Завантажено студентів: {len(student_list)} з {argv[1]}")
    except FileNotFoundError:
        student_list = StudentList()
        print(f"Файл {argv[1]} не знайдено, список порожній")

    while True:
        choice = input("Оберіть дію [ C додати, U змінити, D видалити, P друк, X вихід ] ")
        match choice:
            case "C" | "c":
                add_new_student(student_list)
                student_list.print_all()
            case "U" | "u":
                update_student(student_list)
                student_list.print_all()
            case "D" | "d":
                delete_student(student_list)
            case "P" | "p":
                student_list.print_all()
            case "X" | "x":
                utils.save(student_list)
                print(f"Дані збережено у {argv[1]}")
                break
            case _:
                print("Невірний вибір")


if __name__ == "__main__":
    main()
