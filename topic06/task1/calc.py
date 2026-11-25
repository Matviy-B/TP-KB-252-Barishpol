import logging

from operations import ask_number, ask_operation, calculate

logging.basicConfig(
    filename="calc.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

logging.info("Програму запущено")

while True:
    operation = ask_operation()
    if operation == "exit":
        break
    if operation not in ["+", "-", "*", "/"]:
        print("Невідома операція")
        logging.warning(f"Невідома операція: {operation}")
        continue

    a = ask_number("Перше число: ")
    b = ask_number("Друге число: ")
    logging.info(f"Введено: {a} {operation} {b}")

    try:
        result = calculate(a, operation, b)
        print("Результат:", result)
        logging.info(f"Результат: {result}")
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")
        logging.error("Ділення на нуль")

logging.info("Програму завершено")
print("Роботу завершено")
