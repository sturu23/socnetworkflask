from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class RegisterForm(FlaskForm):
    name = StringField(label='სახელი', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label='მეილი', validators=[DataRequired(), Email()])
    password = PasswordField(label='პაროლი', validators=[DataRequired()])
    confirm_password = PasswordField(label='გაიმეორეთ პაროლის', validators=[DataRequired(), EqualTo('password',message='პაროლი არ ემთხვევა!')])
    secret = StringField(label='საიდუმლო სიტყვა', validators=[DataRequired(),Length(min=1, max=4)])
    submit = SubmitField('Sign Up')

    def validate_email_from_db(self):
        email = self.email.data
        if User.find_by_email(email):
            raise ValidationError('მეილი უკვე არსებობს')


class LoginForm(FlaskForm):
    email = StringField('მეილი', validators=[DataRequired(), Email()])
    password = PasswordField('პაროლი', validators=[DataRequired()])
    submit = SubmitField('ავტორიზაცია')

class PasswordReset(FlaskForm):
    secret = StringField('საიდუმლო სიტყვა', validators=[DataRequired(), Length(min=1, max=4)])
    submit = SubmitField('Reset Password')