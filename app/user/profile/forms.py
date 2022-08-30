from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField





class UploadPhotoForm(FlaskForm):
    photo = FileField('Upload a photo')
    submit2 = SubmitField('Upload')



class RemovePhotoForm(FlaskForm):
    submit = SubmitField('Remove')


class UpdateForm(FlaskForm):
    username = StringField('Name',validators=[DataRequired(), Length(min=2, max=20)])
    proffesion = StringField('Proffesion',validators=[DataRequired(), Length(min=2, max=50)])
    skills = StringField('Skills',validators=[DataRequired(), Length(min=2, max=100)])
    submit1 = SubmitField('Update')