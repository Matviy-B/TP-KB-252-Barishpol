def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, *, /): ")
b = float(input("Введіть друге число: "))

match operation:
    case "+":
        print("Результат:", add(a, b))
    case "-":
        print("Результат:", subtract(a, b))
    case "*":
        print("Результат:", multiply(a, b))
    case "/":
        if b == 0:
            print("Помилка: ділення на нуль")
        else:
            print("Результат:", divide(a, b))
    case _:
        print("Невідома операція")
