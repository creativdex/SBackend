from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.city import CityDB
from app.db.models import Base


class DivisionDB(Base):
    __tablename__ = "division"
    id: Mapped[int] = mapped_column(
        Integer, unique=True, autoincrement=True, nullable=False, primary_key=True
    )
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    city_id: Mapped[int] = mapped_column(Integer, ForeignKey(CityDB.id), nullable=False)
    city = relationship(CityDB, lazy="joined")
