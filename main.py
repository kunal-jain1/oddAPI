from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Enter a number after the slash to check if it is odd."

@app.route('/<string:num>', methods=['GET'])
def get_num(num):
    int_num = int(num)
    num_boolean = None
    if (int_num % 2) == 0:
        num_boolean = False
    else:
        num_boolean = True
    return json.dumps(num_boolean)
