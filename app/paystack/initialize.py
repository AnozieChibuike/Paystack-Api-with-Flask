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
        print("Transaction initialized successfully.")
        print("Response data:")
        print(response.json())
    else:
        print("Transaction initialization failed.")
        print("Response status code:", response.status_code)
        print("Response content:")
        print(response.text)
