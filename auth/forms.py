from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired,EqualTo
   
    
class RegisterForm(FlaskForm):
    full_name = StringField('Name',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Login")
