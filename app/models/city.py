from sqlalchemy import Column, String, Integer
from app.db.models import Base

class CityDB(Base):
    __tablename__ = 'city'
    id: Column = Column(Integer, unique=True, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String, unique=True, nullable=False)




