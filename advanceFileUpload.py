from flask import *
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os

app = Flask(__name__)
app.secret_key = 'bfvwgcUYUGYF YF@#$%^&*(64319[]\pp[]{}:'.encode('utf8')
app.config['upload_folder'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10* 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = ['.jpg','.jpeg','.png']

@app.route('/')
def index():
    images = os.listdir(app.config['upload_folder'])
    pictures = []

    for image in images:

        get_extension = os.path.splitext(image)[1].lower()
        if get_extension in app.config['ALLOWED_EXTENSIONS']:
            pictures.append(image)

    return render_template('uploaded.html', image=pictures)
    
@app.route('/upload')
def upload():       
    return render_template('upload.html')

@app.route('/uploader', methods = ['POST', 'GET'])
def uploader():
    if request.method == 'POST':

        try:

            file = request.files['profilePicture']

            get_extension = os.path.splitext(file.filename)[1].lower()

            if get_extension not in app.config['ALLOWED_EXTENSIONS']:

                return 'file is not an image, <a href="upload">try again</a>'

            if file:

                file.save(os.path.join(

                    app.config['upload_folder'], secure_filename(file.filename)
                    
                    ))
                flash ('uploaded succesfully')
                return redirect(url_for('index'))

        except RequestEntityTooLarge:

            return 'file size is more than 10MB limit <a href="upload">try again</a>'

    return render_template('upload.html')

@app.route('/images/<image>')
def images(image):
    return send_from_directory(app.config['upload_folder'],image)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=3565)