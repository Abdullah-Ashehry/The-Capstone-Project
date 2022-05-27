import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database Heroku
DATABASE_URL = "postgres://uuggfytauonmci:b88f57433f55738871dbc5d336cae951d8c8d82da8d89ccd60bcbb461a88ee2b@ec2-3-211-221-185.compute-1.amazonaws.com:5432/df7u7t3ffkae1n"
os.getenv("{DATABASE_URL}")


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://uuggfytauonmci:b88f57433f55738871dbc5d336cae951d8c8d82da8d89ccd60bcbb461a88ee2b@ec2-3-211-221-185.compute-1.amazonaws.com:5432/df7u7t3ffkae1n'
