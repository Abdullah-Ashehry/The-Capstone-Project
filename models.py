import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate


database_path = 'postgres://uuggfytauonmci:b88f57433f55738871dbc5d336cae951d8c8d82da8d89ccd60bcbb461a88ee2b@ec2-3-211-221-185.compute-1.amazonaws.com:5432/df7u7t3ffkae1n'
# database_path = "postgres://{}/{}".format('localhost:5432', 'capstone')
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)
    db.create_all()


# Thumbnail
# Video
# Name
# Category
# Description
# Year
class Movie(db.Model):
    __tablename__ = 'Movie'
    id = db.Column(db.Integer, primary_key=True)
    thumbnail = db.Column(db.String)
    video = db.Column(db.String)
    name = db.Column(db.String, unique=True, nullable=False)
    category = db.Column(db.String)
    description = db.Column(db.String)
    year = db.Column(db)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'thumbnail': self.thumbnail,
            'video': self.video,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'year': self.year
        }


class Actor(db.Model):
    __tablename__ = 'Actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
