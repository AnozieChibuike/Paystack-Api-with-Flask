from app import app, InitializeTransaction
from flask import request,render_template

@app.route('/', methods=['POST','GET'])
def hello():
    if request.method == 'POST':
        
    return render_template("index.html")

