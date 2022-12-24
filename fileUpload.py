from flask import *
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
    if request.method == 'POST':
        return '<p>Click here to <a href="upload" target="_blank">upload a profile picture</a>'
    
@app.route('/upload')
def upload():       
    return render_template('upload.html')

@app.route('/uploader', methods = ['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        
        file = request.files['profilePicture']
        file.save(secure_filename(file.filename))
        return render_template('uploaded.html')

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)