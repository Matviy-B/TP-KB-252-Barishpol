from operations import ask_number, ask_operation, calculate

while True:
    operation = ask_operation()
    if operation == "exit":
        break
    if operation not in ["+", "-", "*", "/"]:
        print("Невідома операція")
        continue

    a = ask_number("Перше число: ")
    b = ask_number("Друге число: ")

    try:
        print("Результат:", calculate(a, operation, b))
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")

print("Роботу завершено")
