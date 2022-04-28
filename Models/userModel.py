from Conn.db_conection import db

class user(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(9))
    
    def to_json(self):
        return {
                    "id": self.id,
                     "nome": self.nome, 
                     "email": self.email
                }

