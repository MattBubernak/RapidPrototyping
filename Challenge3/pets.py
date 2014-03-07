from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)


class Pets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    gender = db.Column(db.String(120), unique=True)
    age = db.Column(db.Integer)
    speed = db.Column(db.String(120))

    def __init__(self, name, gender, age, speed):
        self.name = name
        self.gender = gender
        self.age = age
        self.speed = speed

    def __repr__(self):
        return 'Name: %r' % str(self.name)

print Pets.query.all()