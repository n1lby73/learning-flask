from flask import Flask, render_template
from form import regForm

app = Flask(__name__)
app.config['SECRET_KEY'] ="trying to work with wtforms"

@app.route('/', methods=['POST','GET'])
def index():
    form=regForm()
    if form.validate_on_submit():
        return "few"
    return render_template('form-index.html',form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)
