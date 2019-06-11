from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class WallForm(FlaskForm):
    name = StringField('name')
    location = SelectField('location')
