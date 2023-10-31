from app import app,paystack
from flask import request,render_template
from random import randint

@app.route('/')
def index():
    return render_template("index.html")

@app.post('/payment/initializePaymentGateway')
def PaystackInit():
    data = request.form
    email = data.get('email')
    amount = data.get('amount')
    reference = str(randint(1000000,99999999))
    init = paystack.InitializeTransaction(email,amount,reference)
    if init[1]:
        return init[0]
    else:
        return init[0]
