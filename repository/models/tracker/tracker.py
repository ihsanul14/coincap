from sqlalchemy import Column, String, Float
from ..models import Base

class Tracker(Base):
    __tablename__ = 'tracker'
    name = Column(String, primary_key=True)
    price = Column(Float)
    usd_price = Column(String)