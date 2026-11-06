def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    first = input("Перше число (або exit для виходу): ")
    if first == "exit":
        break
    operation = input("Операція (+, -, *, /): ")
    second = input("Друге число: ")

    a = float(first)
    b = float(second)

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

print("Роботу завершено")
