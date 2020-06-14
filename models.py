
import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
database_path ='postgresql://3bady@localhost:5432/capstone'
db = SQLAlchemy()
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app,db)
    db.app = app
    db.init_app(app)
    db.create_all()

class Movie(db.Model):
    __tablename__ = 'Movie'
    #__searchable__= ["name","city","state","address"]
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.String(120),nullable=False)
    Actor_id = db.Column(db.Integer ,db.ForeignKey('Actor.id'),nullable=False)
   
class Actor(db.Model):
    __tablename__ = 'Actor'
    #__searchable__= ["name","city","state"]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(120),nullable=False )  
    shows_movie = db.relationship("Movie", backref="Actor")