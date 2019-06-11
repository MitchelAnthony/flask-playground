from flask_wtf import FlaskForm
from wtforms import DateTimeField, SelectField

class AttemptForm(FlaskForm):
    date = DateTimeField('date')
    user = SelectField('user')
    route = SelectField('route')
