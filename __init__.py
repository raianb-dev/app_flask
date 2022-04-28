from flask import Flask
from .Models.userModel import user 
from .Models.Serialize import set_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    msg = {"Alert":"API Connect Successful"}
    return (msg)

@app.route("/user", methods=["GET"])
def select_user():
    usuarios_objetos = user.query.all()
    usuarios_json = [user.to_json() for user in usuarios_objetos]

    return set_response(200, usuarios_json)

