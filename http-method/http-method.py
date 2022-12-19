from flask import Flask, redirect, request, url_for
app = Flask(__name__)

@app.route('/post')
def welcomePage():
    return "You have succesfully connected to the internet"

@app.route('/get')
def declinePage():
    return "Access denied"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        return redirect(url_for(welcomePage))
    else:
        return redirect(url_for(declinePage))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=3565)

# pc going off, have to pause here for today