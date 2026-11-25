import requests


def get_rate(currency):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"
    data = requests.get(url).json()
    return data[0]["rate"]


currency = input("Валюта (EUR, USD, PLN): ").upper()
if currency not in ["EUR", "USD", "PLN"]:
    print("Непідтримувана валюта")
else:
    amount = float(input("Кількість: "))
    rate = get_rate(currency)
    print(f"Курс НБУ: 1 {currency} = {rate} UAH")
    print(f"{amount} {currency} = {round(amount * rate, 2)} UAH")
