from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return "<i>hello world, just wanted to see if i can use html syntax in conjuction with flask</i>"

if __name__== "__main__":
    app.run(port=3565, debug=True, host="0.0.0.0")