@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    zipFilePath = os.path.join(app.config['UPLOAD_FOLDER'], 'sample.zip')
    zipObj = ZipFile('sample.zip', 'w')
    
    if request.method == 'POST':
        for f in request.files:
            if allowed_file(request.files[f].filename):
                filename = secure_filename(request.files[f].filename)
                zipObj.write(request.files[f].filename)
    zipObj.close()
    return 'files uploaded'