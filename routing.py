from flask import Flask
app = Flask(__name__)
@app.route('/test')

def test():
    return "it worked"

if __name__== "__main__":
    app.run(port=3565, debug=True, host="0.0.0.0")