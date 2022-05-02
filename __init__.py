from flask import Flask, request
from .Models.userModel import user, db
from .Models.appSettings import set_response
import datetime


app = Flask(__name__)


@app.route("/")
def home():
    msg = {"alert":"API Connect Successful"}
    return set_response(200, msg)

@app.route("/v1/Account/Users", methods=["GET"])
def userSelect():
    cursor = user.query.all()
    usuarios_json = [user.to_selectJson() for user in cursor]

    if cursor:
        return set_response(200, usuarios_json)
    else:
        msg = 'results not found'
        return set_response(400, usuarios_json, msg)
    
@app.route("/v1/Account/User/<id>", methods=["GET"])
def userId(id):

    cursor = user.query.filter_by(id=id).first()

    if cursor:
        cursor = cursor.to_getJson()
        return set_response(200, cursor)
    else:
        msg = 'user not found'
        return set_response(400, cursor, msg)
    
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
    
    date = str(datetime.datetime.now())
    usuario =  user(
                        name = body["name"],
                        email = body["email"],
                        phone = body["phone"],
                        createdAt = f"{date}"
                    )
    db.session.add(usuario)
    db.session.commit()
    return set_response(200, usuario.to_addJson())

@app.route("/v1/Account/User/<id>", methods=["PUT"])
def update_usuario(id):
    usuario_objeto = user.query.filter_by(id=id).first()
    body = request.get_json()
    date = str(datetime.datetime.now())
    usuario_objeto =  user(
                        name = body["name"],
                        email = body["email"],
                        phone = body["phone"],
                        latUpdatedAt = f"{date}"
                    )

    usuario_objeto.name = body["name"]
    usuario_objeto.email = body["email"]
        
    db.session.update(usuario_objeto)
    db.session.commit()
    return set_response(200, "Updated Successful")