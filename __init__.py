from flask import Flask, Response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    msg = {"Alert":"API Connect Successful"}
    return jsonify(msg)
