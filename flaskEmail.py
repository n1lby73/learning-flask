from flask import *
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'learningflaskemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'sgfdjggjgnmfehjk'
app.config['MAIL_DEFAULT_SENDER'] = ('practice email sending', 'learningflaskemail@gmail.com')
mail = Mail(app)

@app.route('/')
def index():
    return '<a href="email">click here to recieve an email</a>'

@app.route('/email')
def email():
    msg = Message('Testing', recipients=['wparlkvvdqljnvnkcl@tmmbt.com'])
    msg.body = 'did it work'
    mail.send(msg)
    return 'email sent'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)
