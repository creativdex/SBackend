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


@router.get("/get_all", response_model=list[Division])
async def get_all_division(session: AsyncSession = Depends(get_session)):
    division_dal = DivisionDAL(session)
    divisions = await division_dal.get_all()
    if divisions is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body'],
                                    'msg': 'Division not found',
                                    'type': 'value_error'})
    else:
        return divisions


@router.get("/get/{id}", response_model=Division)
async def get_by_id(id: int, session: AsyncSession = Depends(get_session)):
    division_dal = DivisionDAL(session)
    division = await division_dal.get_by_id(id)
    if division is None:
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','id'],
                                    'msg': 'Division not found',
                                    'type': 'value_error'})
    else:
        return division


@router.delete("/delete/{id}", status_code=204)
async def delete_by_id(id: int, session: AsyncSession = Depends(get_session)):
    division_dal = DivisionDAL(session)
    if not await division_dal.get_by_id(id):
        raise HTTPException(status_code=422,
                            detail={'loc': ['body','id'],
                                    'msg': 'Division not found',
                                    'type': 'value_error'})
    await division_dal.delete_by_id(id)