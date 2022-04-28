from .conn.db_conection import db, app

class user(db.Model):
    
    id = db.Column(db.Integer, primary_key= True, unique= True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique= True)
    phone = db.Column(db.String(9))
    bio = db.Column(db.String(100))
    url_pic = db.Column(db.String(100))
    status = db.Column(db.Boolean)

    def to_json(self):
        return {
                    "profile":
                        {
                            "status": self.status,
                            "bio": self.bio,
                            "url_pic": self.url_pic
                            },
                        
                    "id": self.id,
                    "nome": self.name, 
                    "email": self.email
                }


