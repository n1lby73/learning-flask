from flask import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['upload_folder'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10* 1024 * 1024

# @app.route('/')
# def index():
#     return render_template('login.html')

# @app.route('/confirm', methods = ['POST', 'GET'])
# def confirm():
#     if request.method == 'POST':
#         return '<p>Click here to <a href="upload" target="_blank">upload a profile picture</a>'

@app.route('/')
def index():
    return '<p>Click here to <a href="upload" target="_blank">upload a profile picture</a>'
    
@app.route('/upload')
def upload():       
    return render_template('upload.html')

@app.route('/uploader', methods = ['POST', 'GET'])
def uploader():
    if request.method == 'POST':

        file = request.files['profilePicture']

        if file:
            file.save(os.path.join(

                app.config['upload_folder'], secure_filename(file.filename)
                
                ))

            return render_template('uploaded.html')

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)