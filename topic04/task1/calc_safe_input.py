def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def ask_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Помилка: введіть число")


while True:
    operation = input("Операція (+, -, *, /) або exit: ")
    if operation == "exit":
        break
    if operation not in ["+", "-", "*", "/"]:
        print("Невідома операція")
        continue

    a = ask_number("Перше число: ")
    b = ask_number("Друге число: ")

    try:
        if operation == "+":
            print("Результат:", add(a, b))
        elif operation == "-":
            print("Результат:", subtract(a, b))
        elif operation == "*":
            print("Результат:", multiply(a, b))
        else:
            print("Результат:", divide(a, b))
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")

print("Роботу завершено")
