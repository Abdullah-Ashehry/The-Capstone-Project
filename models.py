import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate


# database_path ='postgres://cyusdufwqepfbx:86ff10ea3963bed3ba9a8867168c5e727023c041cd42de3751ff9590ed2c8867@ec2-54-86-170-8.compute-1.amazonaws.com:5432/ddp273p1s8o4pj'
database_path = "postgres://{}/{}".format('localhost:5432', 'capstone')
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):
    __tablename__ = 'Movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.String(120), nullable=False)

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
                'title': self.title,
                'city': self.city,
                'release_date': self.release_date
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
