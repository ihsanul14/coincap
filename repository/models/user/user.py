from sqlalchemy import Column, String
from ..models import Base


class User(Base):
    __tablename__ = 'user'
    email = Column(String, primary_key=True)
    password = Column(String)