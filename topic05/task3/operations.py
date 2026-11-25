from functions import add, subtract, multiply, divide


def ask_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Помилка: введіть число")


def ask_operation():
    return input("Операція (+, -, *, /) або exit: ")


def calculate(a, operation, b):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    else:
        return divide(a, b)
