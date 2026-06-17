import os
import requests  
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}!"}

@app.get("/convert/{from_currency}/{to_currency}/{amount}")
def convert(from_currency: str, to_currency: str, amount: float):
    API_KEY = os.environ.get("EXCHANGE_API_KEY")
    URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(URL)
    data = response.json()
    
    if data.get("result") != "success":
        return {"error": data}
    
    exchange_rate = data["conversion_rates"][to_currency]
    converted_amount = amount * exchange_rate
    return {"from": from_currency, "to": to_currency, "amount": amount, "converted": converted_amount}

class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask")
def ask_ai(request: PromptRequest):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json={
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": request.prompt}]
    })
    your_answer = response.json()["choices"][0]["message"]["content"]
    return {"answer": your_answer}
