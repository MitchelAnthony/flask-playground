from flaskr import db

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(), nullable=True)
    grade = db.Column(db.String(), nullable=True)
    name = db.Column(db.String(), nullable=True)
    wall_id = db.Column(db.Integer, db.ForeignKey('wall.id'), nullable=False)
    attempts = db.relationship('Attempt', backref='attempt', lazy=True)
