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

if operation == "+":
    print("Результат:", add(a, b))
elif operation == "-":
    print("Результат:", subtract(a, b))
elif operation == "*":
    print("Результат:", multiply(a, b))
elif operation == "/":
    if b == 0:
        print("Помилка: ділення на нуль")
    else:
        print("Результат:", divide(a, b))
else:
    print("Невідома операція")
