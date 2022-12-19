from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return "welcome %s" %name

# @app.route('/get')
# def declinePage():
#     return "Access denied"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form("username")
        return redirect(url_for(welcome))
    # else:
    #     return redirect(url_for(declinePage))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=3565)