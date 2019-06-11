from flaskr import db
from flaskr.models import wall

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    walls = db.relationship('Wall', backref='location', lazy=True)
