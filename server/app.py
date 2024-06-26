#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    return f'<h1>{parameter}</h1>'

@app.route('/count/<int:parameter>')
def count(parameter):
    nums=''
    for i in range(parameter):
        nums += str(i) + '<br>'
    return f'<h1>{nums}</h1>'
   

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1,operation,num2):
    if operation == "+":
        answer= num1+num2
    elif operation == "-":
        answer= num1-num2
    elif operation == "*":
        answer= num1*num2
    elif operation == "div":
        answer= num1/num2
    elif operation == "%":
        answer= num1%num2
    
    return f'<h1>{answer}</h1'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
