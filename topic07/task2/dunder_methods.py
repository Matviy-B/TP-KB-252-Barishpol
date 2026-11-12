class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}; {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Empty:
    pass


p1 = Point(3, 4)
p2 = Point(1, 2)

print("__init__:", p1.x, p1.y)
print("__str__ :", p1)
print("__repr__:", [p1, p2])
print("__eq__  :", p1 == Point(3, 4), p1 == p2)
print("__add__ :", p1 + p2)

print("Клас без власних методів:", Empty())
