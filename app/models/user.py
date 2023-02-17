import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.city import CityDB
from app.db.models import Base


class UserDB(Base):
    __tablename__ = 'users'
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tg_id = Column(Integer, unique=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey(CityDB.id), nullable=False)
    city = relationship(CityDB, lazy='joined')
    privileges = Column(Integer, default=1)
