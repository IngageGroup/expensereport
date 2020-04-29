from flask import Flask, flash, json, request, redirect, Response, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import zipstream
import os
from wtforms import Form, StringField, validators


class ReportForm(Form):
    lastname = StringField('lastname', [validators.DataRequired()])
    firstname = StringField('firstname', [validators.DataRequired()])
    year = StringField('year', [validators.DataRequired()])
    month = StringField('month', [validators.DataRequired()])


UPLOAD_FOLDER = '/app/uploads'
ALLOWED_EXTENSIONS = {'gif', 'jpeg', 'jpg', 'pdf', 'png', 'xlsx'}
app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['DEBUG'] = True
app.config['HOST'] = '0.0.0.0'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/ping', methods=['GET'])
def ping():
    response = app.response_class(
        response='pong',
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = ReportForm(request.form)
    isValid = form.validate()
    if request.method == 'POST' and isValid == True:
        z = zipstream.ZipFile(mode='w', compression=zipstream.ZIP_DEFLATED)

        for f in request.files:
            file = request.files[f]
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                z.write(filepath)

        response = Response(z, mimetype='application/zip')
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(
            'files.zip')
        return response
    elif isValid != True:
        return app.response_class(
            response='Bad Request',
            status=400,
            mimetype='application/json'
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
