from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.division import DivisionDB
from app.db.models import Base


class CashboxDB(Base):
    __tablename__ = 'cashbox'
    id: Mapped[int] = mapped_column(Integer, unique=True, autoincrement=True, nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    division_id: Mapped[int] = mapped_column(Integer, ForeignKey(DivisionDB.id), nullable=False)
    division = relationship(DivisionDB,  lazy='joined')




