from flask import Flask, flash, url_for, render_template, redirect, request

app = Flask(__name__)
app.secret_key = 'heruih gxy!@#$%^&*gHFGYE GL#7389875890@!'.encode('utf8')

@app.route('/')
def index():
    return render_template('messageFlashing.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'testadmin' and request.form['password'] == 'admin':
            flash('login successfully')
            return redirect(url_for('user'))
        else:
            flash('username or password is incorrect')
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/user')
def user():
    return render_template('successMessageFlashing.html')

@app.route('/logout')
def logout():
    flash('logged out successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)