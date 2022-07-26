from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Length,ValidationError,DataRequired


class StatiaForm(FlaskForm):
    title = StringField('სათაური',validators=[DataRequired(),Length(min=3,max=20,message='სათაური უნდა შეიცავდეს მაქსიმუმ 20 სიტყვას')])
    content = TextAreaField('სტატია',validators=[DataRequired(),Length(min=15,max=240,message='სტატია უნდა იყოს 15 სიტყვაზე მეტი')])
    submit = SubmitField('გამოქვეყნება')


