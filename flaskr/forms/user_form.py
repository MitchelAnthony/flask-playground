from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class UserForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
