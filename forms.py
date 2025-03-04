from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    content = TextAreaField(validators=[DataRequired()])
    author = StringField(validators=[DataRequired()])