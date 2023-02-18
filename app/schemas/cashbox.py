from pydantic import BaseModel, Field
from app.schemas.division import Division


class CashboxIn(BaseModel):
    name: str
    division_id: int

    class Config:
        orm_mode = True


class Cashbox(CashboxIn):
    id: int
    division_id: int = Field(..., exclude=False)
    division: Division
