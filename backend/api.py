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


ALLOWED_EXTENSIONS = {'gif', 'jpeg', 'jpg', 'pdf', 'png', 'xlsx'}
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config.from_envvar('EXPENSE_REPORT_APP_SETTINGS')
CORS(app)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def save_files(files):


def generate_new_receipt_filename(form, increment, ext):
    return "{}{}_{}_{}_{}_Receipt{}".format(str(form.year.data), str(form.month.data), str(form.lastname.data), str(form.firstname.data), increment, ext)


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
        x = 1
        for f in request.files:
            file = request.files[f]
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                ext = os.path.splitext(filepath)[1]
                newFilePath = os.path.join(
                    app.config['UPLOAD_FOLDER'], generate_new_receipt_filename(form, x, ext))
                os.rename(filepath, newFilePath)
                z.write(newFilePath)
                x += 1

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
