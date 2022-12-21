from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/confirm', methods=['POST','GET'])
def confirm():
    if request.method == 'POST':
        cred = request.form

        print(" ")
        print(cred)
        print (" ")
        
        return render_template('credential.html', show=cred)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3565, debug=True)


