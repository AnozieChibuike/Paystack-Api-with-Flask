import requests
import os
from dotenv import load_dotenv

load_dotenv()

import requests

def VerifyTransaction(reference):
    url = url = f"https://api.paystack.co/transaction/verify/{reference}"
    headers = {
        "Authorization": f"Bearer {os.getenv('PaystackSecretKey')}",
    }

    response = requests.get(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        return [response.json(),True]
    else:
        return [response.json(),False]
