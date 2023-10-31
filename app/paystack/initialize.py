import requests
import os
from dotenv import load_dotenv

load_dotenv()


def InitializeTransaction(email,amount,reference):
    url = "https://api.paystack.co/transaction/initialize"
    headers = {
        "Authorization": f"Bearer {os.getenv('PaystackSecretKey')}",
        "Content-Type": "application/json",
    }
    data = {
        "email": email,
        "amount": amount,
        "reference": reference
    }

    response = requests.post(url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        return list(response.json(),True)
    else:
        return list(response.json(),False)
