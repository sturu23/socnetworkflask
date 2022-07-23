import os

projectdir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'mykey'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(projectdir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

