from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f'hello {username}'
    else:
        return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)