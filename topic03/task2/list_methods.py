numbers = [5, 2, 8]
print("Початковий список:", numbers)

numbers.append(10)
print("append(10)     :", numbers)

numbers.extend([1, 3])
print("extend([1, 3]) :", numbers)

numbers.insert(1, 99)
print("insert(1, 99)  :", numbers)

numbers.remove(8)
print("remove(8)      :", numbers)

numbers.sort()
print("sort()         :", numbers)

numbers.reverse()
print("reverse()      :", numbers)

backup = numbers.copy()
print("copy()         :", backup)

numbers.clear()
print("clear()        :", numbers)
print("Копія після clear():", backup)
