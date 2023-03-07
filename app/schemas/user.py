import re
from uuid import UUID
from pydantic import BaseModel, validator, Field
from app.schemas.city import City


class UserIn(BaseModel):
    tg_id: str | None
    name: str
    phone: str
    city_id: int = Field(..., exclude=True)

    @validator("phone")
    def phone_validator(cls, v):
        if not re.match(r"^\d{10}$", v):
            raise ValueError("Неверный формат номера телефона")
        return v

    class Config:
        orm_mode = True


class User(UserIn):
    user_id: UUID
    city: City
    privileges: int
