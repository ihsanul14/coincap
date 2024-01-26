from framework.database.database import Database
from sqlalchemy.orm import sessionmaker
from ...models import User
from application.middleware import JwtMiddleware
import hashlib


class UserSqllite:
    db = Database().sql_lite()
    def get_data_by_id(self,data:User):
        Session = sessionmaker(bind=self.db)
        session = Session()
        result = {}
        result= session.query(User).filter(
            User.email == data['email'], 
            User.password == self.encrypt_password(data['password']) 
            ).one()
        session.close()
        return result
    
    def sign_in(self, data:User):
        data = {
            'email': data.email
        }
        token = JwtMiddleware().generate_token(data)
        res = {
            'token': token,
        }
        return res


    def add_data(self,data):
        Session = sessionmaker(bind=self.db)
        session = Session()
        query = User(email=data[
            'email'],password=self.encrypt_password(data['password']))
        session.add(query)
        session.commit()
        session.close()
        return data 

    def delete_data(self,data):
        Session = sessionmaker(bind=self.db)
        session = Session()
        query = session.query(User).filter(User.email == data['email']).one()
        session.delete(query)
        session.commit()
        session.close()
        return data
    
    def encrypt_password(self, data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        hashed_data = sha256_hash.hexdigest()
        return hashed_data
