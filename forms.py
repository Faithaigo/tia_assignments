from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired,EqualTo


class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    
class RegisterForm(FlaskForm):
    full_name = StringField('Name',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    password = PasswordField('Confirm password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")