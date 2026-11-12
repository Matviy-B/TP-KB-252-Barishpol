import math


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def solve_quadratic(a, b, c):
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        return (-b / (2 * a),)
    else:
        return ()


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

roots = solve_quadratic(a, b, c)
if len(roots) == 2:
    print("Два корені: x1 =", roots[0], ", x2 =", roots[1])
elif len(roots) == 1:
    print("Один корінь: x =", roots[0])
else:
    print("Дійсних коренів немає")
