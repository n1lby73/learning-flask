from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/')
def cookieHomePage():
    return render_template('cookieLogin.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    user = request.form['username']
    login = request.form['password']
    resp = make_response(render_template('successfulCookieLogin.html'))
    resp.set_cookie('userDetails2', login)
    resp.set_cookie('userDetails', user)
    return resp

@app.route('/getcookie')
def getcookies():
    loggedpassword = request.cookies.get('userDetails2')
    loggeduser = request.cookies.get('userDetails')
    return 'your username is %s and your logged password is %s' %(loggeduser, loggedpassword)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=3565)
