import requests
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}
prompt = input("Enter your prompt: ")

response = requests.post(url, headers=headers, json={
    "model": "llama-3.3-70b-versatile",
    "messages": [{"role": "user", "content": prompt}]
})
your_answer = response.json()["choices"][0]["message"]["content"]

print(your_answer)