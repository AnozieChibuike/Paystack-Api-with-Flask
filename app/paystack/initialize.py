import requests
import os
from dotenv import load_dotenv

load_dotenv()


def InitializeTransaction(email,amount,reference,callback_url=None):
    url = "https://api.paystack.co/transaction/initialize"
    headers = {
        "Authorization": f"Bearer {os.getenv('PaystackSecretKey')}",
        "Content-Type": "application/json",
    }
    data = {
        "email": email,
        "amount": int(str(amount + '00')),
        "reference": reference,
        "callback_url": callback_url
    }
    
    response = requests.post(url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        return [response.json(),True]
    else:
        return [response.json(),False]
        