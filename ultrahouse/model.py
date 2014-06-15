from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    mac = db.Column(db.Unicode)
