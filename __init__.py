

from flask import Flask, request
from numpy import tri
from sqlalchemy import exists, null, true
from .Models.userModel import User, db 
from .Models.Serialize import set_response


app = Flask(__name__)

@app.route("/")
def home():
    msg = {"alert":"API Connect Successful"}
    return set_response(200, msg)

@app.route("/v1/Account/Users", methods=["GET"])
def userSelect():
    usuarios_objetos = User.query.all()
    usuarios_json = [User.to_selectJson() for User in usuarios_objetos]

    return set_response(200, usuarios_json)

@app.route("/v1/Account/User/<id>", methods=["GET"])
def userId(id):
    cursor = User.query.filter_by(id=id).first()
    user = cursor.to_getJson()

    return set_response(200, user)

@app.route("/v1/Account/User", methods=["POST"])
def userAdd():
    body =  request.get_json()
    try:
        if body["name"] is not body:
            pass
    except Exception as msg:
        msg = "name is required"
        return set_response(400,None, msg)

    try:
        if body["email"] is not body:
            pass
    except Exception as msg:
        msg = "email is required"
        return set_response(400,None, msg)

    try:
        if body["phone"] is not body:
            pass
    except Exception as msg:
        msg = "phone is required"
        return set_response(400,None, msg)

    usuario =  User(
                        name = body["name"],
                        email = body["email"],
                        phone = body["phone"],
                        bio = body["bio"],
                        url_pic = body["url_pic"]
                    )
    db.session.add(usuario)
    db.session.commit()
    return set_response(200, usuario.to_addJson())
