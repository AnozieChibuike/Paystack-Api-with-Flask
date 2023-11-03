from app import app,paystack
from flask import request,render_template, redirect,session,flash
from random import randint
bal = 0
@app.route('/')
def index():
    global bal
    return render_template("index.html",bal=bal)

@app.post('/payment/initializePaymentGateway')
def PaystackInit():
    data = request.form
    email = data.get('email')
    amount = data.get('amount')
    reference = str(randint(1000000,99999999))
    try:
        init = paystack.InitializeTransaction(email,amount,reference,callback_url=f'http://localhost:5000/verify_transaction')
        if init[1]:
            return redirect(init[0]['data']['authorization_url'])
        else:
            return init[0]
    except:
        return "Err something went wrong with tour connection"
@app.route('/verify_transaction')
def verify():
    global bal
    data = request.args.get
    reference = data('reference')
    
    init = paystack.VerifyTransaction(reference)
    if init[0]['status']:
        bal += (init[0]['data']['amount']/100)
        flash('success')
        return redirect('/')
    else:
        flash('failed')
        return redirect('/')
# @app.route('/successful')
# def success():
    
