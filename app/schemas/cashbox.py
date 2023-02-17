from pydantic import BaseModel


class Cashbox(BaseModel):
    id: int
    name: str
    id_division: int
