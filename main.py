
from flask import Flask
from models.userModel import user
from models.conn_mysql.db_conection import session
from models.appSettings.config_json import response


app = Flask(__name__)

@app.route("/")
def home():
    msg = {"alert":"API Connect Successful"}
    return response(200, msg)


@app.route("/v1/Account/Users", methods=["GET"])
def userSelect():
    to_getUser = user.to_getUser(user.to_getUser)
    query = [to_getUser for instace in session.query(user).order_by(user.id)]
    return response(200, query)