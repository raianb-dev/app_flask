from flask import Flask, request
from .Models.userModel import user, db
from .Models.Serialize import set_response

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

    usuario =  user(
                        name = body["name"],
                        email = body["email"],
                        phone = body["phone"]
                    )
    db.session.add(usuario)
    db.session.commit()
    return set_response(200, usuario.to_addJson())