from pydantic import BaseModel, Field
from app.schemas.city import City


class DivisionIn(BaseModel):
    name: str
    id_city: int

    class Config:
        orm_mode = True


class Division(DivisionIn):
    id: int
    name: str
    id_city: int = Field(...,exclude=False)
    city: City
