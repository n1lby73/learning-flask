from flask import Flask, redirect, request, url_for
app = Flask(__name__)

@app.route('/')
def homepage():
    return redirect(url_for("login"))

@app.route('/login')
def login():

   return '<form action="method" method="get"> <input type="text" name="username" placeholder="press enter on your keyboard after typing"/> </form>'

@app.route('/post')
def welcomePage():
    return "You have succesfully connected to the internet"

@app.route('/get')
def declinePage():
    return "Access denied"

@app.route('/method', methods=['POST','GET'])
def method():

    if request.method == 'POST':
        return redirect(url_for("welcomePage"))
    else:
        return redirect(url_for("declinePage"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=3565)
