from flask import Flask

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    return "#"
