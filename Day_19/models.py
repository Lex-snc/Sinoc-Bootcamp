from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(80), nullable=True)
    confirm_password = db.Column(db.String(80), nullable=True)
    fname = db.Column(db.String(80), nullable=True)
    lname = db.Column(db.String(80), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(80), nullable=True)
    bday = db.Column(db.String(80), nullable=True)

