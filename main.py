import requests  
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}!"}

@app.get("/convert/{from_currency}/{to_currency}/{amount}")
def convert(from_currency: str, to_currency: str, amount: float):
    API_KEY = '49205777a2f9846f3119bdc2'
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(URL)
    data = response.json()
    exchange_rate = data["conversion_rates"][to_currency]
    converted_amount = amount * exchange_rate
    return {"from": from_currency, "to": to_currency, "amount": amount, "converted": converted_amount}
