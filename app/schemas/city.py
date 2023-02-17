from pydantic import BaseModel


class CityIn(BaseModel):
    name: str

    class Config:
        orm_mode = True


class City(CityIn):
    id: int




