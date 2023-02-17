from pydantic import BaseModel
from user import UserOut
from division import Division
from cashbox import Cashbox


class Appeal(BaseModel):
    id: int
    type_appeal: str
    user: UserOut
    division: Division
    description: str | Cashbox | None
    files: str | None
    status: bool = False
