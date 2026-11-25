def find_insert_position(numbers, value):
    low = 0
    high = len(numbers)
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] < value:
            low = mid + 1
        else:
            high = mid
    return low


data = [1, 3, 5, 7, 9, 11]
print("Список:", data)

for value in [0, 4, 7, 12]:
    position = find_insert_position(data, value)
    print(f"Значення {value} -> позиція {position}")
    data.insert(position, value)
    print("Список після вставки:", data)
