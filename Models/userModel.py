from ..Models.conn.db_conection import db

class user(db.Model):
    __tablename__ = 'Account'
    
    id = db.Column(db.Integer, primary_key= True, unique= True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique= True)
    phone = db.Column(db.String(9))
    bio = db.Column(db.String(100))
    url_pic = db.Column(db.String(100))
    status = db.Column(db.Boolean)

    def to_getJson(self):
        return {
                    "account":
                        {
                            "id": self.id,
                            "name": self.name, 
                            "email": self.email
                            },
                    "status": self.status,
                    "bio": self.bio,
                    "url_pic": self.url_pic
            }
    def to_addJson(self):
        return {
                    "userId": self.id,
           
        }
    def to_selectJson(self):
        return {
            "userId": self.id,
            "name": self.name,
            "url_pic": self.url_pic
        }


