from sqlalchemy import create_engine as ce
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, Column, String
from flask import Flask


engine = ce('mysql://root:@localhost/_database', echo=True)
base = declarative_base()
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()
session._model_changes = {}

base = Flask(base)

