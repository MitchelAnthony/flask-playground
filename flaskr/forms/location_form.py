from flask_wtf import FlaskForm
from wtforms import StringField

class LocationForm(FlaskForm):
    name = StringField('name')
