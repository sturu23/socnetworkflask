from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField





class UploadPhotoForm(FlaskForm):

    photo = FileField('Upload a photo')
    submit = SubmitField('Upload')


class RemovePhotoForm(FlaskForm):
    submit = SubmitField('Remove')

