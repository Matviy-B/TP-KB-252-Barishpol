class Operation:
    symbol = ""

    def execute(self, a, b):
        pass


class Add(Operation):
    symbol = "+"

    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    symbol = "-"

    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    symbol = "*"

    def execute(self, a, b):
        return a * b


class Divide(Operation):
    symbol = "/"

    def execute(self, a, b):
        return a / b
