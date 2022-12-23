from flask import Flask, session, url_for, request, redirect, render_template

app = Flask(__name__)

app.secret_key = 'hg fz757*UR*(!YGHFUkoijxeiuhg'.encode('utf8')

@app.route("/")
def index():
    if 'user' in session:
        return 'you are already logged in <a href="/logout" target="_blank">click here to log out</a>'
    return "<a href='/login'>login here</a>"


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        session['user'] = request.form['username']
        return redirect(url_for('index'))

    return render_template('sessionlogin.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3565, debug=True)