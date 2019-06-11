from flaskr import db

class Wall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    locationid = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    routes = db.relationship('Route', backref='route', lazy=True)
