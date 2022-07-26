from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/<string:num>', methods=['GET'])
def get_num(num):
    int_num = int(num)
    num_boolean = True
    if (int_num % 2) == 0:
        num_boolean = False
    return json.dumps(num_boolean)

@app.route('/shields/<string:num>', methods=['GET'])
def get_shield_info(num):
    int_num = int(num)
    num_boolean = True
    if (int_num % 2) == 0:
        num_boolean = False
    dict = {'schemaVersion:', 1, 'label:', 'is it odd', 'message:', num_boolean, 'color', 'green'}
    return json.dumps(dict)

if __name__ == "__main__":
    app.run(debug=True)