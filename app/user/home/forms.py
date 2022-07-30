from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Length,ValidationError,DataRequired


class StatiaForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired(),Length(min=3,max=50,message='მიუთითეთ სათაური')])
    content = TextAreaField('Content',validators=[DataRequired(),Length(min=15,max=240,message='სტატია უნდა იყოს 15 სიტყვაზე მეტი')])
    submit = SubmitField('Post')


