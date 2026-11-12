try:
    int("abc")
except ValueError as error:
    print("ValueError:", error)

try:
    "2" + 2
except TypeError as error:
    print("TypeError:", error)

try:
    print(10 / 0)
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as error:
    print("IndexError:", error)

try:
    person = {"name": "Олена"}
    print(person["age"])
except KeyError as error:
    print("KeyError:", error)

try:
    open("no_such_file.txt")
except FileNotFoundError as error:
    print("FileNotFoundError:", error)
