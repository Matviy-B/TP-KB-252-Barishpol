priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def is_number(token):
    return token not in priority and token not in ("(", ")")


def add_number(tokens, number):
    if number == "-":
        raise ValueError("Невірний вираз")
    tokens.append(number)


def tokenize(expression):
    tokens = []
    number = ""
    for char in expression:
        if char.isdigit() or char == ".":
            number += char
            continue
        if number != "":
            add_number(tokens, number)
            number = ""
        if char == " ":
            continue
        if char == "-" and (len(tokens) == 0 or tokens[-1] == "(" or tokens[-1] in priority):
            number = "-"
        elif char in priority or char in "()":
            tokens.append(char)
        else:
            raise ValueError("Невідомий символ: " + char)
    if number != "":
        add_number(tokens, number)
    return tokens


def to_rpn(tokens):
    output = []
    stack = []
    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while len(stack) > 0 and stack[-1] != "(":
                output.append(stack.pop())
            if len(stack) == 0:
                raise ValueError("Неузгоджені дужки")
            stack.pop()
        else:
            while len(stack) > 0 and stack[-1] != "(":
                top = stack[-1]
                if priority[top] > priority[token] or (priority[top] == priority[token] and token != "^"):
                    output.append(stack.pop())
                else:
                    break
            stack.append(token)
    while len(stack) > 0:
        top = stack.pop()
        if top == "(":
            raise ValueError("Неузгоджені дужки")
        output.append(top)
    return output


def calculate(rpn):
    stack = []
    for token in rpn:
        if is_number(token):
            stack.append(float(token))
            continue
        if len(stack) < 2:
            raise ValueError("Невірний вираз")
        b = stack.pop()
        a = stack.pop()
        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        elif token == "*":
            stack.append(a * b)
        elif token == "/":
            stack.append(a / b)
        else:
            stack.append(a ** b)
    if len(stack) != 1:
        raise ValueError("Невірний вираз")
    return stack[0]


def main():
    while True:
        expression = input("Введіть вираз (exit для виходу): ")
        if expression == "exit":
            break
        try:
            rpn = to_rpn(tokenize(expression))
            print("ЗПН:", " ".join(rpn))
            result = calculate(rpn)
            if result == int(result):
                result = int(result)
            print("Результат:", result)
        except ZeroDivisionError:
            print("Помилка: ділення на нуль")
        except ValueError as error:
            print("Помилка:", error)


if __name__ == "__main__":
    main()
