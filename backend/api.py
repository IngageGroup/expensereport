from flask import Flask, flash, json, request, redirect, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '/app/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'}
app = Flask(__name__)
app.secret_key='super secret key'
app.config['DEBUG']=True
app.config['HOST']='0.0.0.0'
app.config['SESSION_TYPE']='filesystem'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
CORS(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/ping', methods=['GET'])
def ping():
    data = {
        'ping': 'yes'
    }
    response = app.response_class(
        response='pong',
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for f in request.files:
            file = request.files[f]
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'files uploaded'
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
