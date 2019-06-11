from flaskr import db
from flaskr.models import blog, attempt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    blogs = db.relationship('Blog', backref='user', lazy=True)
    attempts = db.relationship('Attempt', backref='user', lazy=True)
