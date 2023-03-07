from pydantic import BaseModel, Field
from uuid import UUID
from app.schemas.user import User
from app.schemas.division import Division
from app.schemas.type_of_problem import TypeOfProblem


class AppealIn(BaseModel):
    type_of_problem_id: int
    user_id: UUID
    division_id: int
    description: str
    files: str | None

    class Config:
        orm_mode = True


class Appeal(AppealIn):
    id: int
    type_of_problem: TypeOfProblem = Field(exclude={'is_show'})
    user: User
    division: Division = Field(exclude={'city'})
    description: str
    files: str | None
    status: bool | None
    type_of_problem_id: int = Field(exclude=True)
    user_id: UUID = Field(exclude=True)
    division_id: int = Field(exclude=True)
