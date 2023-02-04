import os
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

class linkAppDb(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return (f"linkAppDb('{self.username}', '{self.email}')")

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

    new_user = linkAppDb(username=username, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(success=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', debug=True, port=3566)