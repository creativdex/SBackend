from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.city import CityDB
from app.db.models import Base


class DivisionDB(Base):
    __tablename__ = 'division'
    id: Column = Column(Integer, unique=True, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey(CityDB.id), nullable=False)
    city = relationship(CityDB,  lazy='joined')




