from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models import Base

class CityDB(Base):
    __tablename__ = 'city'
    id: Mapped[int] = mapped_column(Integer, unique=True, autoincrement=True, nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)




