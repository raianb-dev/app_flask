from pyexpat import model
from .conn_mysql.db_conection import session, engine, base
from sqlalchemy import Column, Integer, String, Boolean

class user(base.model):
    __tablename__ = 'account'
    
    id = Column(Integer, primary_key= True, unique= True)
    name = Column(String(50))
    email = Column(String(100), unique= True)
    phone = Column(String(9))
    bio = Column(String(100))
    url_pic = Column(String(100))
    status = Column(Boolean)
    createdAt = Column(String(60))
    latUpdatedAt = Column(String(60))


    def to_getUser(self):
        return {
                    "account":
                        {
                            "id": self.id,
                            "name": self.name, 
                            "email": self.email
                            },
                    "status": self.status,
                    "bio": self.bio,
                    "url_pic": self.url_pic,
                    "createdAt": self.createdAt,
                    "lastedUpdate": self.latUpdatedAt
            }

    def to_post(self):
        return {
                    "userId": self.id,
           
        }
        
    def to_getProfile(self):
        return {
            "userId": self.id,
            "name": self.name,
            "url_pic": self.url_pic
        }

    

#base.metadata.drop_all(engine)
#base.metadata.create_all(engine)