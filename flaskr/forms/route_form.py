from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class RouteForm(FlaskForm):
    color = StringField('color') # Should this be a select?
    grade = StringField('grade') # Should this also be a select? 
    name = StringField('name')
    wall = SelectField('wall')
