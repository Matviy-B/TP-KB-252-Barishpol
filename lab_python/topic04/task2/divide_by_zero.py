def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")
        return None


print(divide(10, 2))
print(divide(7, 0))
print(divide(0, 5))
