# Currency Converter API 🚀

## What it does

This is a simple Currency Converter API built using FastAPI. It provides endpoints to greet users and convert currency amounts using real-time exchange rates from an external API.

## Technologies Used

* Python
* FastAPI
* Requests Library
* ExchangeRate API
* Uvicorn

## Features

* Home endpoint
* Personalized greeting endpoint
* Real-time currency conversion
* REST API architecture
* JSON responses

## How to Run

1. Install the required packages:

```bash
pip install fastapi uvicorn requests
```

2. Save the code as `main.py`.

3. Start the server:

```bash
uvicorn main:app --reload
```

4. Open your browser and visit:

```text
http://127.0.0.1:8000
```

5. To access the API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Home

```http
GET /
```

Response:

```json
{
  "message": "Hello World"
}
```

### Greeting

```http
GET /greet/Chiru
```

Response:

```json
{
  "message": "Hello Chiru!"
}
```

### Currency Conversion

```http
GET /convert/USD/INR/100
```

Response:

```json
{
  "from": "USD",
  "to": "INR",
  "amount": 100,
  "converted": 8550.0
}
```

## API Used

This project uses ExchangeRate API to fetch live currency exchange rates.

Website:
https://www.exchangerate-api.com/

## Future Improvements

* Better error handling
* Support for invalid currency codes
* Currency list endpoint
* Conversion history
* Database integration

##

Created by Chiru jayanth 
