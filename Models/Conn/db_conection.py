from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

connMod = app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
connURI = app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/_database'

db = SQLAlchemy(app)