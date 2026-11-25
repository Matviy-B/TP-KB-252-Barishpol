from operations import Add, Subtract, Multiply, Divide


class Calculator:
    def __init__(self):
        self.operations = {}
        self.history = []
        for operation in [Add(), Subtract(), Multiply(), Divide()]:
            self.operations[operation.symbol] = operation

    def calculate(self, a, symbol, b):
        result = self.operations[symbol].execute(a, b)
        self.history.append(f"{a} {symbol} {b} = {result}")
        return result
