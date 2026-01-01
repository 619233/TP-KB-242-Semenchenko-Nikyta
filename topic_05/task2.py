import requests 

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

data = response.json()

options = ["EUR", "USD", "PLN"]

user_input = input("Введи EUR, USD або PLN: ").strip().upper()

if user_input not in options:
            print(f"Помилка: Вибери одне з значень: {options}")
            exit()

user_amount = float(input("Введи суму у цій валюті (розмежувальний знак - крапка): "))

for elem in data:
    if elem['cc'] == user_input:
        result = elem['rate'] * user_amount
        
        print(f"Курс {user_input}: {elem['rate']}")
        print(f"До отримання: {round(result, 2)} грн")
        break