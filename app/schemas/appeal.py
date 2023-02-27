from pydantic import BaseModel
from user import UserOut
from division import Division
from cashbox import Cashbox
from type_of_problem import TypeOfProblem


class Appeal(BaseModel):
    id: int
    type_of_problem: TypeOfProblem
    user: UserOut
    division: Division
    description: str | Cashbox | None
    files: str | None
    status: bool = False
