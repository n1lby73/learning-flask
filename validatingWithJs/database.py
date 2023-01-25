from flask import Flask, render_template, url_for, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method != 'POST':
        return redirect(url_for('index'))
    
    data = request.get_json()

    username = data["username"]
    email = data["email"]
    password = data["password"]

    return jsonify(success=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)