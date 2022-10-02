from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Length,ValidationError,DataRequired


class StatiaForm(FlaskForm):
    content = TextAreaField('Content',validators=[DataRequired(),Length(min=5,max=240,message='სტატია უნდა იყოს 5 სიტყვაზე მეტი')])

    submit = SubmitField('Post')



