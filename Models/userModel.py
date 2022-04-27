
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/agend'

db = SQLAlchemy(app)

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    
    
    def to_json(self):
        return {
                    "id": self.id,
                     "nome": self.nome, 
                     "email": self.email
                }
