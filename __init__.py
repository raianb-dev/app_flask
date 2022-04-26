from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    msg = {"Alert":"API Connect Successful"}
    return jsonify (msg)
