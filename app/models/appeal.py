from datetime import datetime
from sqlalchemy import String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.models import Base
from app.models.type_of_problem import TypeOfProblemDB
from app.models.user import UserDB
from app.models.division import DivisionDB


class AppealDB(Base):
    __tablename__ = "appeal"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dt_start: Mapped[datetime] = mapped_column(
        Date, nullable=False, default=datetime.now()
    )
    dt_finish: Mapped[datetime] = mapped_column(
        Date, nullable=True
    )
    type_of_problem_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(TypeOfProblemDB.id), nullable=False
    )
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), ForeignKey(UserDB.user_id), nullable=False
    )
    division_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(DivisionDB.id), nullable=False
    )
    description: Mapped[str] = mapped_column(String, nullable=False)
    files: Mapped[str] = mapped_column(String, nullable=True)
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    type_of_problem = relationship(TypeOfProblemDB, lazy="joined")
    user = relationship(UserDB, lazy="joined")
    division = relationship(DivisionDB, lazy="joined")
