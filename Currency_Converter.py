import requests


def convert(from_currency: str, to_currency: str, amount: float):
    API_KEY = '49205777a2f9846f3119bdc2'
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(URL)
    data = response.json()
    
    
    if data['result'] == 'success':
        exchange_rate = data["conversion_rates"][to_currency]
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        print("Error fetching exchange rates:", data["error-type"])
        return None
    
from_currency = input("Enter the currency you want to convert from (e.g., USD): ")
to_currency = input("Enter the currency you want to convert to (e.g., EUR): ")
amount = float(input("Enter the amount to convert: "))


converted_amount = convert_currency(from_currency, to_currency, amount)
if converted_amount is not None:
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")