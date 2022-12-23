from flask import Flask, redirect, url_for, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('errorLogin.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'testadmin' and request.form['password'] == 'admin':
            return redirect(url_for('authorized'))
        else:
            #error handling with the abort function
            abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/authorized')
def authorized():
    return 'you have successfully logged in'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)