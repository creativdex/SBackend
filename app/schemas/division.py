from pydantic import BaseModel, Field
from app.schemas.city import City


class DivisionIn(BaseModel):
    name: str
    city_id: int

    class Config:
        orm_mode = True


class Division(DivisionIn):
    id: int
    name: str
    city_id: int = Field(..., exclude=True)
    city: City
