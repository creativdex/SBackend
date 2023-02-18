from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dals.division import DivisionDAL
from app.schemas.division import Division, DivisionIn
from app.db.session import get_session

router = APIRouter()


@router.post("/add_division", response_model=Division)
async def add_division(body: DivisionIn,
                       session: AsyncSession = Depends(get_session)):
    division_dal = DivisionDAL(session)
    new_division = await division_dal.create_division(body)
    return new_division
