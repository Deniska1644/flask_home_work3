from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, unique=False, nullable=True)
