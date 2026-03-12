import requests

url = "http://127.0.0.1:5000/predict"

transaction = {
    "amount": 90000,
    "transaction_type": "transfer",
    "old_balance": 100000,
    "new_balance": 10000
}

response = requests.post(url, json=transaction)

print(response.json())
