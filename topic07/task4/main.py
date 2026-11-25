from calculator import Calculator


def ask_number(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Помилка: введіть число")


calc = Calculator()

while True:
    symbol = input("Операція (+, -, *, /) або exit: ")
    if symbol == "exit":
        break
    if symbol not in calc.operations:
        print("Невідома операція")
        continue

    a = ask_number("Перше число: ")
    b = ask_number("Друге число: ")

    try:
        print("Результат:", calc.calculate(a, symbol, b))
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")

print("Історія обчислень:")
for line in calc.history:
    print(line)
