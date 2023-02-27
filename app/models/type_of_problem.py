from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models import Base


class TypeOfProblemDB(Base):
    __tablename__ = "type_of_problem"
    id: Mapped[int] = mapped_column(
        Integer, unique=True, nullable=False, primary_key=True
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    is_show: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )
