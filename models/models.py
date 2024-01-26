from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    email = Column(String, primary_key=True)
    password = Column(String)


class CreateUserRequest(BaseModel):
    email: constr(strict=True, min_length=1)
    password: constr(strict=True, min_length=1)
    
class UpdateUserRequest(BaseModel):
    email: constr(strict=True, min_length=1)
    password: constr(strict=True, min_length=1)
