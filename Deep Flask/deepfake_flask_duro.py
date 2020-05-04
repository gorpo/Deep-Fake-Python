# -*- coding: utf-8 -*-
import os
import time
import hashlib

from flask import Flask, render_template, redirect, url_for, request
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import deepfake



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gorpo'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'images') # you'll need to create a folder named uploads

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, 'Image Only!'), FileRequired('Choose a file!')])
    submit = SubmitField('Upload')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        for filename in request.files.getlist('photo'):
            name = 'deep_fake'
            photos.save(filename, name=name + '.')
        success = True
    else:
        success = False
    return render_template('index.html', form=form, success=success)


@app.route('/manage')
def manage_file():
    files_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    return render_template('manage.html', files_list=files_list)


@app.route('/open/<filename>')
def open_file(filename):
    file_url = photos.url(filename)
    return render_template('browser.html', file_url=file_url)


@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = photos.path(filename)
    os.remove(file_path)
    return redirect(url_for('manage_file'))

#deep fake------------>>
@app.route('/a/<filename>')
def deepnude(filename):
    #ativa o deep nudes
    inputpath = photos.path(filename)
    out = filename
    deepfake.main(inputpath,out)
    #retorna imagem aberta
    nome = out.strip('.jpg')
    retorno_imagem = f'{nome}_renderizada.jpg'

    file_url2 = photos.url(retorno_imagem)
    return render_template('browser.html', file_url=file_url2)



if __name__ == '__main__':
    app.run(debug=True)