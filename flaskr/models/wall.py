from flaskr import db
from flaskr.models import location, route

class Wall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    routes = db.relationship('Route', backref='wall', lazy=True)
