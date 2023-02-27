from pydantic import BaseModel, Field


class TypeOfProblemIn(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class TypeOfProblem(TypeOfProblemIn):
    is_show: bool