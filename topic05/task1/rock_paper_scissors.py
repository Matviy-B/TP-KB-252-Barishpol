import random

choices = ["stone", "scissor", "paper"]
wins = {"stone": "scissor", "scissor": "paper", "paper": "stone"}

user = input("Ваш вибір (stone, scissor, paper): ")
while user not in choices:
    print("Некоректне значення")
    user = input("Ваш вибір (stone, scissor, paper): ")

computer = random.choice(choices)
print("Комп'ютер обрав:", computer)

if user == computer:
    print("Нічия")
elif wins[user] == computer:
    print("Ви перемогли!")
else:
    print("Комп'ютер переміг!")
