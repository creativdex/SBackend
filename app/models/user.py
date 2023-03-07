import uuid
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.city import CityDB
from app.db.models import Base


class UserDB(Base):
    __tablename__ = "users"
    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    tg_id: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    phone: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    city_id: Mapped[int] = mapped_column(Integer, ForeignKey(CityDB.id), nullable=False)
    city = relationship(CityDB, lazy="joined")
    privileges: Mapped[int] = mapped_column(Integer, default=1)
