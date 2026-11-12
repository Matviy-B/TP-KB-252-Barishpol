def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

print("D =", discriminant(a, b, c))
