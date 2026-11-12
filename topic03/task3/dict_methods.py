person = {"name": "Олена", "age": 20}
print("Початковий словник:", person)

person.update({"age": 21, "city": "Чернігів"})
print("update()    :", person)

del person["city"]
print("del         :", person)

print("keys()      :", list(person.keys()))
print("values()    :", list(person.values()))
print("items()     :", list(person.items()))

person.clear()
print("clear()     :", person)
