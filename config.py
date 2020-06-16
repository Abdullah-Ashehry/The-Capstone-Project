import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
DATABASE_URL = "DATABASE_URL: postgres://oofzndxbaqljfk:41be0a2aff85bd4071bddededcc1dddaf0b891aa67836b2b2cc5e162715c44a8@ec2-18-214-211-47.compute-1.amazonaws.com:5432/d3l8590hnlmeji"
os.getenv("{DATABASE_URL}")


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://3bady@localhost:5432/capstone'
