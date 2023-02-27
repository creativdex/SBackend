import re
import uuid
from pydantic import BaseModel, validator, Field
from app.schemas.city import City


class UserIn(BaseModel):
    tg_id: int | None
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


class UserOut(UserIn):
    user_id: uuid.UUID
    city: City
    privileges: int
