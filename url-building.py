from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def urlUser1():
    return "Welcome back to github n1lby73"


@app.route('/guest/<username>')
def urlUser2(username):
    return "hello %s, welcome to n1lby73 github page" %username


@app.route("/home/<linkedname>")
def homepage(linkedname):

    admins = ['n1lby73', 'stanley','stancylee']

    for access in admins:
        
        if linkedname == access:
            return redirect(url_for('urlUser1'))
        else:
            return redirect(url_for('urlUser2', username=linkedname))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)