from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return "hello world, i'm learning flask"

if __name__== "__main__":
    app.run(port=3565, debug=True, host="0.0.0.0")

